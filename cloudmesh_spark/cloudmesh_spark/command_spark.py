import subprocess
from pprint import pprint
import time


class command_spark(object):
    @classmethod
    def deploy(cls, name, count, login, cloud, flavor, image):
	subprocess.call("cm label --prefix=%s"% (name), shell=True)
        output = subprocess.check_output("cm label", shell=True)
        start_index = int(output.split("_")[-1])
        nodes = []
        for i in range (start_index, start_index + int(count)):
            nodes.append(name + "_" + str(i)) 
        subprocess.call("cm cluster create %s --count=%s --ln=%s --cloud=%s --flavor=%s --image=%s"% (name, count, login, cloud, flavor, image), shell=True)
        subprocess.call("rm $CM_SPARK_DIR/inventory/%s_inventory.txt"% (name), shell=True)
        subprocess.call("rm $CM_SPARK_DIR/node_keys/%s"% (name), shell=True)
        subprocess.call("rm $CM_SPARK_DIR/node_keys/%s.pub"% (name), shell=True)
        subprocess.call("echo \"[spark-cluster]\" > $CM_SPARK_DIR/inventory/%s_inventory.txt"% (name), shell=True)
        subprocess.call("ssh-keygen -t rsa -f $CM_SPARK_DIR/node_keys/%s -P \"\""% (name), shell=True)
        slaves = "\n"
        ip_list = []
        for node in nodes:
            subprocess.call("cm vm ip assign %s"% (node), shell=True)
            time.sleep(2)
            output = subprocess.check_output("cm vm ip show %s --format=json"% (node), shell=True)
            ip = output.split("\n")[4].split(":")[1].split("\"")[1]
            slaves += ip + "\n"
            ip_list.append(ip)
            subprocess.call("echo \"%s\" >> $CM_SPARK_DIR/inventory/%s_inventory.txt"% (ip, name), shell=True)
            subprocess.call("scp $CM_SPARK_DIR/node_keys/%s ubuntu@%s:~/.ssh/id_rsa"% (name, ip), shell=True)
            subprocess.call("scp $CM_SPARK_DIR/node_keys/%s.pub ubuntu@%s:~/.ssh/id_rsa.pub"% (name, ip), shell=True)
            subprocess.call("ssh-copy-id -i $CM_SPARK_DIR/node_keys/%s ubuntu@%s"% (name, ip), shell=True)
        for ip_address in ip_list:
            subprocess.call("ssh ubuntu@%s \'exit\'"% (ip_address), shell=True)

        subprocess.call("ansible-playbook -i $CM_SPARK_DIR/inventory/%s_inventory.txt -c ssh $CM_SPARK_DIR/ansible/spark.yaml"% (name), shell=True)

        for ip_address in ip_list:
            subprocess.call("ssh ubuntu@%s \'echo \"%s\" >> /home/ubuntu/spark-1.3.1-bin-hadoop2.6/conf/slaves.template\'"% (ip_address, slaves), shell=True)
            

    @classmethod
    def destroy(cls, name):
        subprocess.call("cm cluster remove %s"% (name), shell=True)

    
    @classmethod
    def start(cls, master):
        output = subprocess.check_output("cm vm ip show %s --format=json"% (master), shell=True)
        ip = output.split("\n")[4].split(":")[1].split("\"")[1]
        subprocess.call("ssh ubuntu@%s \'bash /home/ubuntu/spark-1.3.1-bin-hadoop2.6/sbin/start-all.sh\'"% (ip), shell=True)


    @classmethod
    def stop(cls, master):
        output = subprocess.check_output("cm vm ip show %s --format=json"% (master), shell=True)
        ip = output.split("\n")[4].split(":")[1].split("\"")[1]
        subprocess.call("ssh ubuntu@%s \'bash /home/ubuntu/spark-1.3.1-bin-hadoop2.6/sbin/stop-all.sh\'"% (ip), shell=True)

