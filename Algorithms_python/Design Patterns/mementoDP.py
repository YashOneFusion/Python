"""Memento class for saving the data"""
import datetime

class Memento:
	def __init__(self, state) -> None:
		self.state=state

class TimeMachine:
	def __init__(self) -> None:
		self._state="" 

	def write(self, state):
		self._state=state

	def saveToMemento(self):
		return Memento(self._state)
	
	def undo(self, memento):
		self._state=memento.state

class Caretaker:
	def save(self, writer):
		self.obj=writer.saveToMemento()

	def undo(self, writer):
		writer.undo(self.obj)

careTaker = Caretaker()
writer = TimeMachine()
writer.write("Teleported to 1000AD\n")
careTaker.save(writer)
print(writer._state)

writer.write("Teleported to 5BC\n")
print(writer._state)
print("Oops! wrong time zone; Teleporting to previous given time\n")
careTaker.undo(writer)
print(writer._state)
