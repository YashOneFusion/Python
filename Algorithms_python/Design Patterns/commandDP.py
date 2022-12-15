#Command ABC(Abstract Base Class) class
# Implementation for Command class
#  Receiver class
# Invoker class

from abc import ABC

class Command(ABC):

    def __init__(self, receiver):
        self.receiver= receiver
    def process(self):
        pass

class CmdImplementation(Command):

    def __init__(self, receiver):
        self.receiver=receiver
    def process(self):
        print("Command Interface: executing the Command in Receiver now...\n")
        self.receiver.perform_command()

class Receiver:

    def perform_command(self):
        print("Receiver: executing Command...\n")
        print("Command Invoked in Receiver Successfully\n\n")
    
class Invoker:

    def invokeCmd(self, cmd):
        self.cmd = cmd
    def executeCmd(self):
        print("Invoking Command Interface...\n")
        self.cmd.process()

if __name__=='__main__':
    rec=Receiver()
    cmd = CmdImplementation(rec)
    invoker=Invoker()
    invoker.invokeCmd(cmd)
    invoker.executeCmd()
