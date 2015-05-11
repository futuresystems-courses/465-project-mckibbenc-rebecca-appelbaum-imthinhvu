import subprocess
from pprint import pprint


class command_spark(object):
    @classmethod
    def deploy(cls, name, count = 3, login = "ubuntu", cloud = "india", flavor = "m1.small", image = "futuresystems/ubuntu-14.04"):
	subprocess.call("cm label --prefix=%s"% (name), shell=True)
        subprocess.call("cm cluster create %s --count=%s --ln=%s --cloud=%s --flavor=%s --image=%s"% (name, count, login, cloud, flavor, image), shell=True)

    @classmethod
    def destroy(cls, name):
        subprocess.call("cm cluster remove %s"% (name), shell=True)
