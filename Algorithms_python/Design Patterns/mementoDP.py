"""Memento class for saving the data"""

class Memento:

	def __init__(self, content):

		# self.file = file
		self.content = content

class FileWriterUtility:

	def __init__(self):
		# self.file = file
		self.content = ""
	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.content)

	def undo(self, memento):
		# self.file = memento.file
		self.content = memento.content
class FileWriterCaretaker:
	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':

	"""create the caretaker object"""
	caretaker = FileWriterCaretaker()

	"""create the writer object"""
	writer = FileWriterUtility()

	"""write data into file using writer object"""
	writer.write("First vision of GeeksforGeeks\n")
	print(writer.content + "\n\n")

	"""save the file"""
	caretaker.save(writer)

	"""again write using the writer """
	writer.write("Second vision of GeeksforGeeks\n")

	print(writer.content + "\n\n")

	"""undo the file"""
	caretaker.undo(writer)

	print(writer.content + "\n\n")
