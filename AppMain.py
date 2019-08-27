from Database import Student, InnitializeStudents , ExamStats ,StatsStudents , Session
from Database import Exams , InnitializeExams
from menus import Main
from tools import Strings, Lists
students = InnitializeStudents.all()
exams = InnitializeExams.all()

print("The Database has been Loaded. press any key to continue..")
input()
print(Student.describe("elvis"))