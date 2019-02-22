from Institution.InterLink.Internship import Internship
from Institution.University import University
from Person.Knowledge import Knowledge
from Person.Student import Student

knowledge_high_level = Knowledge(5)
knowledge_low_level = Knowledge(3)

s = Student("Alex")
s.SetKnowlendge(knowledge_high_level)
university = University("CH.U.I.")
university.AddStudent(Student("Andrew Kostenko", knowledge_high_level))
university.AddStudent(Student("Julia Veselkina", knowledge_high_level))
university.AddStudent(Student("Maria Perechrest", knowledge_low_level))
university.AddStudent(s)

internship = Internship("Interlink")
internship.InvitationsToInternship(university)
print("List of internship's students:")
print(internship.GetStudents())