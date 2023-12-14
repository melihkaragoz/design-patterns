from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def display(self):
        pass


class Factory(ABC):
    def createStudent(self):
        pass

    def createTeacher(self):
        pass


class Student(User):
    def display(self):
        return "I'm a Student"


class Teacher(User):
    def display(self):
        return "I'm a Teacher"


class UserFactory(Factory):
    def createStudent(self):
        return Student()

    def createTeacher(self):
        return Teacher()


# Create new factory for create users
factory = UserFactory()

# Create a student and use it's display method
student = factory.createStudent()
print(student.display())

# Create a teacher and use it's display method
teacher = factory.createTeacher()
print(teacher.display())

