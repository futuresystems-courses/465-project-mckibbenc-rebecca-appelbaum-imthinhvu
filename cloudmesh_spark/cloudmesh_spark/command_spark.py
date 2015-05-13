import subprocess
from pprint import pprint


class command_spark(object):
    @classmethod
    def deploy(cls, name, count = 3, login = "ubuntu", cloud = "india", flavor = "m1.small", image = "futuresystems/ubuntu-14.04"):
	subprocess.call("cm label --prefix=%s"% (name), shell=True)
        output = subprocess.check_output("cm label", shell=True)
        start_index = int(output.split("_")[-1])
        nodes = []
        for i in range (start_index, start_index + count):
            nodes.append(name + "_" + str(i)) 
        subprocess.call("cm cluster create %s --count=%s --ln=%s --cloud=%s --flavor=%s --image=%s"% (name, count, login, cloud, flavor, image), shell=True)
        for node in nodes:
            subprocess.call("cm vm ip assign %s"% (node), shell=True)	

    @classmethod
    def destroy(cls, name):
        subprocess.call("cm cluster remove %s"% (name), shell=True)
