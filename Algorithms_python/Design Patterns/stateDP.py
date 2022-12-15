import sys
sys.setrecursionlimit(10)
#context
#State
#Invoker / Interface
class interface:
    def __init__(self, state):
        self.state=state

class StateB(interface):
    def __init__(self) -> None:
        print('Called state from State A\n')
        print('Switching to State Quit')
        self.state=StateQuit()

class StateA(interface):
    def __init__(self) -> None:
        print("Current state: A")
        print('Switching to B\n')
        self.state=StateB()

class StateQuit(interface):
    def __init__(self) -> None:
        print("Quitting...\n")

print("\n Example of Switching to different states:\n")
StateA()
