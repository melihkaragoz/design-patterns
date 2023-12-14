from copy import deepcopy

class Lesson:
    def clone(self):
        pass

class CreateLesson(Lesson):
    def __init__(self, value):
        self.branch = value

    def clone(self):
        return deepcopy(self)

lesson = CreateLesson("Undefined")

copy1 = lesson.clone()
copy2 = lesson.clone()

copy1.branch = "Guitar"
copy2.branch = "Piano"

print(f"Original branch: {lesson.branch}")
print(f"Copy 1 branch: {copy1.branch}")
print(f"Copy 2 branch: {copy2.branch}")