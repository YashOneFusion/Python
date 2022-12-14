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
        self.receiver.perform_command()

class Receiver:

    def perform_command(self):
        print("Command Invoked in Receiver")
    
class Invoker:

    def invokeCmd(self, cmd):
        self.cmd = cmd
    def executeCmd(self):
        self.cmd.process()

if __name__=='__main__':
    rec=Receiver()
    cmd = CmdImplementation(rec)
    invoker=Invoker()
    invoker.invokeCmd(cmd)
    invoker.executeCmd()
