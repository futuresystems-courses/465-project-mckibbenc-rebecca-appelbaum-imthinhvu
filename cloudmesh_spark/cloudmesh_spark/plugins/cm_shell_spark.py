from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command
from pprint import pprint

from cloudmesh_spark.command_spark import command_spark


class cm_shell_spark:

    def activate_cm_shell_spark(self):
        self.register_command_topic('mycommands', 'spark')

    @command
    def do_spark(self, args, arguments):
        """
        ::

          Usage:
              spark deploy NAME [--count=N] 
                                [--ln=S] 
                                [--cloud=S]
                                [--flavor=S]
                                [--image=S]
              spark destroy NAME
              spark start MASTER
              spark stop MASTER

          Arguments:

            NAME      Name of the spark cluster group
            MASTER    Name of the spark master node

          Options:

             --count=N  number of nodes to create
             --ln=S     login name
             --cloud=S  cloud to use
             --flavor=S flavor to use
             --image=S  image to use

        """
        pprint(arguments)
        if arguments['deploy']:
            Console.ok("Deploying...")
            name = arguments['NAME']
            count = arguments['--count']
            if count is None:
                count = "3"
                print("using default count: " + count)
            ln = arguments['--ln']
            if ln is None:
                ln = "ubuntu"
                print("using default login: " + ln)
            cloud = arguments['--cloud']
            if cloud is None:
                cloud = "india"
                print("using default cloud: " + cloud)
            flavor = arguments['--flavor']
            if flavor is None:
                flavor = "m1.small"
                print("using default flavor: " + flavor)
            image = arguments['--image']
            if image is None:
                image = "futuresystems/ubuntu-14.04"
                print("using default image: " + image)
            command_spark.deploy(name, count, ln, cloud, flavor, image)
        elif arguments['destroy']:
            Console.ok("Destroying...")
            name = arguments['NAME']
            command_spark.destroy(name)
        elif arguments['start']:
            master = arguments['MASTER']
            Console.ok("Starting spark cluster from master node %s"% (master))
            command_spark.start(master)
        elif arguments['stop']:
            master = arguments['MASTER']
            Console.ok("Stopping spark cluster from master node %s"% (master))
            command_spark.stop(master)
        elif arguments["NAME"] is None:
            Console.error("Please specify a name for the cluster")
        else:
            Console.error("Invalid spark command")
        pass

if __name__ == '__main__':
    command = cm_shell_spark()
    command.do_spark("iu.edu")
    command.do_spark("iu.edu-wrong")
