import subprocess
from pprint import pprint


class command_spark(object):
    @classmethod
    def deploy(cls, name, count, login, cloud, flavor, image):
        output = subprocess.check_output("cm label", shell=True)
        start_index = int(output.split("_")[-1])
        nodes = []
        for i in range (start_index, start_index + int(count)):
            nodes.append(name + "_" + str(i)) 
        subprocess.call("cm cluster create %s --count=%s --ln=%s --cloud=%s --flavor=%s --image=%s"% (name, count, login, cloud, flavor, image), shell=True)
        subprocess.call("rm %s_nodes.txt"% (name), shell=True)
        subprocess.call("touch %s_nodes.txt"% (name), shell=True)
        subprocess.call("echo \'%s\\n\' | ssh-keygen -t rsa -P \"\""% (name), shell=True)
        subprocess.call("eval $(ssh-agent) && ssh-add", shell=True)
	subprocess.call("cm label --prefix=%s"% (name), shell=True)
        for node in nodes:
            subprocess.call("cm vm ip assign %s"% (node), shell=True)
            output = subprocess.check_output("cm vm ip show %s --format=json"% (node), shell=True)
            ip = output.split("\n")[4].split(":")[1].split("\"")[1]
            subprocess.call("echo \"%s\" >> $HOME/%s_nodes.txt"% (ip, name), shell=True)
            subprocess.call("scp %s ubuntu@%s:~/.ssh/id_rsa"% (name, ip), shell=True)
            subprocess.call("scp %s.pub ubuntu@%s:~/.ssh/id_rsa.pub"% (name, ip), shell=True)
            subprocess.call("ssh-copy-id -i %s ubuntu@%s"% (name, ip), shell=True)


    @classmethod
    def destroy(cls, name):
        subprocess.call("cm cluster remove %s"% (name), shell=True)
