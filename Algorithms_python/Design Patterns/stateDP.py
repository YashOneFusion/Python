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
        print('Called state from State A')
        self.state=StateA()

class StateA(interface):
    def __init__(self) -> None:
        print('Called state from B')
        self.state=StateB()

StateA()
