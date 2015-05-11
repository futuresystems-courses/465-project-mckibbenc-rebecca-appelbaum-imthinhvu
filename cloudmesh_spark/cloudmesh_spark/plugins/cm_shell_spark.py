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

          Arguments:

            NAME      Name of the spark cluster group

          Options:

             --count=N  number of nodes to create
             --ln=S     login name
             --cloud=S  cloud to use
             --flavor=S flavor to use
             --image=S  image to use

        """
        pprint(arguments)
        if arguments['deploy']:
            Console.ok("I want to deploy")
            name = arguments['NAME']
            count = arguments['--count']
            ln = arguments['--ln']
            cloud = arguments['--cloud']
            flavor = arguments['--flavor']
            image = arguments['--image']	
            command_spark.deploy(name)
        elif arguments['destroy']:
            Console.ok("I want to destroy")
            name = arguments['NAME']
            command_spark.destroy(name)
        elif arguments["NAME"] is None:
            Console.error("Please specify a name for the cluster")
        else:
            name = arguments["NAME"]
            Console.info("trying to reach {0}".format(name))
            status = command_spark.status(name)
            if status:
                Console.info("machine " + name + " has been found. ok.")
            else:
                Console.error("machine " + name + " not reachable. error.")
        pass

if __name__ == '__main__':
    command = cm_shell_spark()
    command.do_spark("iu.edu")
    command.do_spark("iu.edu-wrong")
