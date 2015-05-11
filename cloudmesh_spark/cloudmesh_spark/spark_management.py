import cloudmesh


def CreateCluster(name, count = "3", cloud = "india", flavor = "m1.small", image = "futuresystems/ubuntu-14.04", login = "ubuntu"):
    print(cloudmesh.shell("cluster create %s --count=%s --ln=%s --cloud=%s --flavor=%s --image=%s"% (name, count, login, cloud, flavor, image)))


def RemoveCluster(name):
    print(cloudmesh.shell("cluster remove %s"% (name)))
