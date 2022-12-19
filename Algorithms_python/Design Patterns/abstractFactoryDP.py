# Python Code for object
# oriented concepts using
# the abstract factory
# design pattern
#Credits: GeeksForGeeks
import random

class Course_At_GFG:
	def __init__(self, courses_factory = None):
		"""course factory is out abstract factory"""
		
		self.course_factory = courses_factory
		print(type(self.course_factory))
	def show_course(self):
		course = self.course_factory()
		print(type(course))
		print(f'We have a course named {course}')

		print(f'its price is {course.Fee()}')


class DSA:

	def Fee(self):
		return 11000

	def __str__(self):
		return "DSA"

class STL:

	def Fee(self):
		return 8000

	def __str__(self):
		return "STL"

class SDE:
	def Fee(self):
		return 15000

	def __str__(self):
		return 'SDE'

def random_course():
	return random.choice([SDE, STL, DSA])()


if __name__ == "__main__":

	course = Course_At_GFG(random_course)
	for i in range(5):
		course.show_course()
