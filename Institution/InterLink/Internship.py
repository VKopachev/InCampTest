from Institution.University import University

class Internship:
    def __init__(self, name:str):
        self.name = name
        self.students = []

    def GetStudents(self) -> str:
        # Get students names from list students
        students_names = map(lambda student:student.name, self.students)
        return '\n'.join(self.students)