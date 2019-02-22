from Person import Student

class University:
    def __init__(self, name:str):
        self.name = name
        self.students:Student = []
    
    def AddStudent(self, student:Student):
        self.students.append(student)