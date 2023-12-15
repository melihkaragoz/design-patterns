class Lesson:
    def __init__(self):
        self.branch = None
        self.teacher = None
        self.classroom = None
        self.date = None
        
    def __str__(self):
        return f"{self.teacher}/ {self.branch}"


class LessonBuilder:
    def build_branch(self):
        pass
    def build_teacher(self):
        pass
    def build_classroom(self):
        pass
    def build_date(self):
        pass
    def get_lesson(self):
        pass


class MathLessonBuilder(LessonBuilder):

    def __init__(self):
        self.lesson = Lesson()

    def build_branch(self):
        self.lesson.branch = "Math"

    def build_classroom(self):
        self.lesson.classroom = "CR-4"

    def build_teacher(self):
        self.lesson.teacher = "John Doe"

    def build_date(self):
        self.lesson.date = "20/12/2023"

    def get_lesson(self):
        return self.lesson

class LessonDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_lesson(self):
        self.builder.build_branch()
        self.builder.build_classroom()
        self.builder.build_teacher()
        self.builder.build_date()
        
builder = MathLessonBuilder()
director = LessonDirector(builder)

director.construct_lesson()
lesson = builder.get_lesson()

print(lesson)