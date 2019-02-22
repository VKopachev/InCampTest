from Person import Knowledge

class Student:
    def __init__(self, name:str, knowledge:Knowledge=None):
        self.name = name
        self.knowledge = knowledge
    
    def SetKnowlendge(self, knowledge:Knowledge):
        self.knowledge = knowledge