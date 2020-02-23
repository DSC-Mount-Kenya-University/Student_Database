# The Database should not be modified without proper configuration
import os
from tools import Lists, Strings, Files
# Written by Elvis

class Student(object):
    def __init__(self, name, age, level, cos):
        self.name = name
        self.age = age
        self.level = level
        self.cos = cos
    def __str__(self):
        return self.name
    def save(self):
        update_line = self.name + "," + str(self.age) + "," + str(self.level) + "," + self.cos + "\n"
        file2 = open("studentDB", "r+")
        readf = file2.readlines()
        readf2 = readf
        file2.close()
        file2 = open("studentDB","a")
        print(readf)
        try:
            for item in readf2:
                if self.name in item.strip("\n"):
                    print("Student Already exists!!")
                    return "DUPLICATE"
            file2.write(update_line)
        except:
            return "ERROR"

    def describe(self):
        try:
            hold = "Name :" + self.name + "\n" + "Course :" + self.cos + "\nLevel :" + str(self.level)
            hold = hold + "\nAge :" + str(self.age)
            return hold
        except:
            file = open("studentDB", "r+")
            contents = file.readlines()
            listhold = Lists.strip_from_items(contents, "\n")
            for item in listhold:
                if self in item:
                    print("found record! for", self)
                    templist = item.split(",", 3)
                    s_name = templist[0]
                    age = templist[1]
                    level = templist[2]
                    cos = templist[3]
                    hold = "Name :" + s_name + "\n" + "Course :" + cos + "\nLevel :" + str(level)
                    hold = hold + "\nAge :" + str(age)
                    return hold


    def get_level(self):
        level = self.level
        return level

    def get_age(self):
        age = self.age
        return age

    def get_name(self):
        name = self.name
        return name

    def is_student(self):
        try:
            hold = self.name
            return "true"
        except:
            return "false"

    class Queries:
        def pint_studentdb():
            file = open("studentDB","r+")
            content = file.read()
            return content

        def student_search(name):
            file = open("studentDB","r+")
            contents = file.read()
            hold = contents.split("\n",1)
            db_list = hold
            for item in db_list:
                try:
                    if name.name in item:
                        return item
                except:
                    if name in item:
                        return item
            return "Student Not Found"

        def getstudent_data(name):
            file = open("studentDB", "r+")
            contents = file.readlines()
            listhold = Lists.strip_from_items(contents,"\n")
            for item in listhold:
                try:
                    if name in item:
                        print("found record! for",name)
                        templist = item.split(",",3)
                        s_name = templist[0]
                        age = templist[1]
                        level = templist[2]
                        cos = templist[3]
                        student_dic = {"name": s_name, "course": cos, "level": level, "age": age}
                        return student_dic
                except:
                    if name.name in item:
                        print("found record!",name.name)
                        templist = item.split(",",3)
                        s_name = templist[0]
                        age = templist[1]
                        level = templist[2]
                        cos = templist[3]
                        student_dic = {"name": s_name, "course": cos, "level": level, "age": age}
                        return student_dic

        def get_student_list():
            file = open("studentDB" ,"r+")
            temp = file.readlines()
            temp = Lists.strip_from_items(temp,"\n")
            return temp

        class Alter:

            def remove(name):
                file = open("studentDB","r+")
                filedata = file.readlines()
                filedata2 = filedata
                file.close()
                file = open("studentDB","w")
                try:
                    for item in filedata2:
                        if name.name in item:
                            filedata.remove(item)
                            print("Deleting", name.name)
                    for item in filedata:
                        file.write(item)
                except:
                    for item in filedata2:
                        if name in item:
                            filedata.remove(item)
                            print("Deleting", name)
                    for item in filedata:
                        file.write(item)

            def update(name, age, level, cos,):
                update_line = name + "," + str(age)+"," + str(level) + "," + cos + "\n"
                print(update_line)
                print("UPDATING...")
                file = open("studentDB", "r+")
                filedata = file.readlines()
                filedata2 = filedata
                file.close()
                file = open("studentDB", "w")
                try:
                    for item in filedata2:
                        if name in item:
                            filedata.remove(item)
                            print("Deleting", name)
                    for item in filedata:
                        file.write(item)
                    file.close()
                    file = open("studentDB","a")
                    file.write(update_line)
                    file.close()
                    print(name,"Has been Updated")
                    return
                except:
                    print("An error occured")


class Exams:
    def __init__(self, title, path_to_file):
        self.title = title
        self.path = path_to_file

    def save_exam(exam):
        try:
            exam_file = open("examsDB", "r+")
            temp = exam_file.read()
        except:
            exam_file = open("examsDB", "w+")
            temp = exam_file.read()
        try:
            if exam.title in temp:
                print("Exam Record already exists!!")
            else:
                writeln = exam.title + "$" + exam.path + "\n"
                exam_file.writelines(writeln)
                exam_file.close()
                print("Added ", exam.title, "From path :", exam.path)
        except:
            if exam.title in temp:
                print("Exam Record already exists!!")
            else:
                writeln = exam.title + "$" + exam.path + "\n"
                exam_file.writelines(writeln)
                exam_file.close()
                print("Added ",exam.title, "From path :", exam.path)

    def remove_exam(exam):
        exam_file = open("examsDB","r+")
        temp = exam_file.readlines()
        temp2 = temp
        print(temp)
        exam_file.close()
        exam_file = open("examsDB", "w")
        try:
            for item in temp2:
                if exam.title in item:
                    print("Deleting...", exam.title)
                    temp.remove(item)
                    print(exam.title, "has been removed")
                    pass
                else:
                    pass
            exam_file.write("")
            for item in temp:
                exam_file.writelines(item)
        except:
            for item in temp2:
                if exam in item:
                    print("Deleting...", exam)
                    temp.remove(item)
                    print(exam, "has been removed")
                    pass
                else:
                    pass
            exam_file.write("")
            for item in temp:
                exam_file.writelines(item)

    def update_exam(title,path):
        writeline = str(title) + "$" + str(path) + "\n"
        exam_file = open("examsDB", "r+")
        temp = exam_file.readlines()
        temp2 = temp
        print(temp)
        exam_file.close()
        exam_file = open("examsDB", "w")
        try:
            for item in temp2:
                if title in item:
                    print("Updating...", title)
                    temp.remove(item)
                    print(title, "has been updated")
                    pass
                else:
                    pass
            exam_file.write("")
            for item in temp:
                exam_file.writelines(item)
            exam_file.write(writeline)
        except:
            print("DATABASE ERROR @", title)

    def get_exam_data(exam):
        file = open("examsDB","r+")
        temp = file.readlines()
        for item in temp:
            try:
                if exam.title in item:
                    hold = item.split("$", 1)
                    title = hold[0]
                    path = hold[1].strip("\n")
                    dic = {"title": title, "path": path}
                    print("FETCHING...", exam.title, "from database")
                    return dic
            except:
                if exam in item:
                    hold = item.split("$", 1)
                    title = hold[0]
                    path = hold[1].strip("\n")
                    dic = {"title": title, "path": path}
                    print("FETCHING...", exam, "from database")
                    return dic
                pass

    def get_all_string():
        file = open("examsDB", "r+")
        temp = file.read()
        print("Reading exams Database")
        return temp

    def get_exam_list():
        file = open("examsDB", "r+")
        temp = file.readlines()
        print("Reading list from Exams Database")
        return temp


class ExamStats(Student, Exams):

    def update_exam_stat_for_student(object,object2 ,score):
        try:
            file = open("examStatDB", "r+")
            writeline = object.name + "$" + object2.title + "$" + str(score) + "\n"
            temp = file.readlines()
            temp = Lists.strip_from_items(temp,"\n")
            file.close()
            file = open("examStatDB", "a")
            wrote ="false"
        except:
            file = open("examStatDB", "w+")
            writeline = object.name + "$" + object2.title + "$" + str(score) + "\n"
            temp = file.readlines()
            temp = Lists.strip_from_items(temp, "\n")
            file.close()
            file = open("examStatDB", "a")
            wrote = "false"
        if temp == []:
            file.write(writeline)
            file.close()
        else:
            for item in temp:
                if object.name + "$" + object2.title in item:
                    print("Updating", object.name, "for", object2.title)
                    Files.delete_line_from_file("examStatDB", object.name + "$" + object2.title)
                    file.write(writeline)
                    wrote = "true"
                    break
            if wrote != "true":
                file.write(writeline)

        # listing exams
        student_exams = []
        print("loading...")
        for item in temp:
            if object.name in item.strip("\n"):
                student_exams.append(item.strip("\n"))
            student_exams = Lists.strip_from_items(student_exams,"\n")


class StatsStudents(Student):

    def update_rank():
        try:
            exam_record = StatsStudents.get_all_stats()
            minidb = []
            for record in exam_record:
                examlist = record['exams']
                exam_count = 0
                total = 0
                for exam in examlist:
                    exam_count += 1
                scorelist = record['scores']
                for score in scorelist:
                    total = total + int(score)
                hold = {"name": record['name'], "exams_done": exam_count, "total": total}
                minidb.append(hold)
            print(minidb)

        except:
            file = open("RankDB","w+")
            temp = file.readlines()


    def update_stats(object, level, list_exams_stat):

        try:
            file = open("studentStatDB", "r+")
            temp = file.readlines()
            itemlist = "["
        except:
            file = open("studentStatDB", "w+")
            temp = file.readlines()
            itemlist = "["
        n = 0
        for item in list_exams_stat:
            if n != 0:
                itemlist = itemlist + "," +item
            else:
                itemlist = itemlist + item
            if n == len(list_exams_stat) - 1:
                itemlist = itemlist + "]"
                print("Closing pack")
            n = n +1
        print(itemlist)
        temp = Lists.strip_from_items(temp, "\n")
        writeline = str(object.name) + "$" + str(level) + "$" + itemlist + "\n"
        file.close()
        file = open("studentStatDB", "a")
        wrote = "false"
        if temp == []:
            print("null...Creating Stat file for...", object.name)
            file.write(writeline)
            print("Updating Student Records")
            Student.Queries.Alter.update(object.name,object.age,level,object.cos)
        else:
            for item in temp:
                if object.name in item:
                    print("Updating...>>", object.name)
                    Files.delete_line_from_file("studentStatDB",object.name)
                    file.write(writeline)
                    print("Updating Student Records")
                    Student.Queries.Alter.update(object.name, object.age, level, object.cos)
                    wrote = "true"
                    break
            if wrote != "true":
                file.write(writeline)

    def get_stats(self):
        file = open("studentStatDB","r")
        temp = file.readlines()
        temp = Lists.strip_from_items(temp,"\n")
        try:
            for item in temp:
                for item in temp:
                    if self.name in item:
                        hold1 = item.split("$", 2)
                        hold = hold1[2]
                        n = 0
                        hold = str(hold)
                        if hold == '':
                            n = 1
                        for charcter in hold:
                            if ',' in charcter:
                                n += 1
                        exam_stat = str(hold).replace("[", "").replace("]", "").split(",", n - 0)
                        exams = 1
                        var = ''
                        hold_list = []
                        scores = []
                        exam_list = []
                        for item in exam_stat:
                            hold_list = item.split("$", 2)
                            var = var + "\n" + str(exams) + ". " + hold_list[1] + "...Score : " + hold_list[2]
                            exam_list.append(hold_list[1])
                            scores.append(hold_list[2])
                            exams += 1
                        print(Strings.fomart(var, hold_list[0] + "'s " + "Exam Catalogue"))
                        name = self.name
                        dic = {"name": name, "exam_list": exam_list, "scores": scores}
                        return dic
        except AttributeError:
            print("string evaluation")
            for item in temp:
                if self in item:
                    hold1 = item.split("$",2)
                    hold = hold1[2]
                    n = 0
                    hold = str(hold)
                    if hold == '':
                        n = 1
                    for charcter in hold:
                        if ',' in charcter:
                            n += 1
                    exam_stat = str(hold).replace("[","").replace("]","").split(",",n-0)
                    exams = 1
                    var = ''
                    hold_list = []
                    scores = []
                    exam_list = []
                    for item in exam_stat:
                        hold_list = item.split("$",2)
                        var = var + "\n" + str(exams) + ". " + hold_list[1] + "...Score : " + hold_list[2]
                        exam_list.append(hold_list[1])
                        scores.append(hold_list[2])
                        exams += 1
                    print(Strings.fomart(var, hold_list[0] + "'s " + "Exam Catalogue"))
                    name = self
                    dic = {"name":name,"exam_list":exam_list,"scores":scores}
                    return dic
    def get_all_stats():
        file = open('examStatDB','r')
        temp = file.readlines()
        temp = Lists.strip_from_items(temp,"\n")
        examlist = []
        for item in temp:
            hold = item.split("$",2)
            examlist.append(hold)
        print(examlist)


class InnitializeStudents:

    def all(printf = 'yes'):
        try:
            print("\n\nLoading from Student Database...>>>>>>>>>>>>")
            file = open("studentDB", "r+")
            temp = file.readlines()
            temp = Lists.strip_from_items(temp, "\n")
            students = []
            for item in temp:
                templist = (item.split(",",3))
                templist[0] = Student(templist[0], templist[1], templist[2], templist[3])
                if printf == 'yes':
                    print(str(temp.index(item)+1),"---",templist[0].name)
                students.append(templist[0])
                templist.clear()
            print("..................................................\nCompleted[100%]\n")
            return students
        except:
            print("\n\nLoading from Student Database...>>>>>>>>>>>>")
            file = open("studentDB", "w+")
            temp = file.readlines()
            temp = Lists.strip_from_items(temp, "\n")
            students = []
            for item in temp:
                templist = (item.split(",", 3))
                templist[0] = Student(templist[0], templist[1], templist[2], templist[3])
                print(str(temp.index(item)+1),"---",templist[0].name)
                students.append(templist[0])
                templist.clear()
            print("..................................................\nCompleted[100%]\n")
            return students


class InnitializeExams:
    def all():
        try:

            print("\n\nLoading from Exams Database...>>>>>>>>>>>>>>")
            file = open("examsDB","r+")
            temp = file.readlines()
            temp = Lists.strip_from_items(temp, "\n")
            exams = []
            for item in temp:
                templist = item.split("$", 1)
                templist[0] = Exams(templist[0],templist[1])
                print(templist[0].title, "is now a",templist[0])
                exams.append(templist[0])
                templist.clear()
            print("...............................................\nCompleted[100%]\n")
            return exams
        except:
            print("\n\nLoading from Exams Database...>>>>>>>>>>>>>>")
            file = open("examsDB", "w+")
            temp = file.readlines()
            temp = Lists.strip_from_items(temp, "\n")
            exams = []
            for item in temp:
                templist = item.split("$", 1)
                templist[0] = Exams(templist[0], templist[1])
                print(templist[0].title, "is now a", templist[0])
                exams.append(templist[0])
                templist.clear()
            print("...............................................\nCompleted[100%]\n")
            return exams
class Session(Student, Exams):

    def create_session(student_object, password):
        _active_users = []
        found = 'no'
        if _active_users == []:
            try:
                hold = student_object.name
                print("ACCOUNT HOLDER : ", hold)
                print("__________________\n")
            except AttributeError:
                print("String search...")
                list_students = InnitializeStudents.all('No printing')
                for student in list_students:
                    if student_object in student.name:
                        print("found match", student.name)
                        if student.name in _active_users:
                            print("User session already active!")
                            return student.name + ":" + "active"
                        else:
                            found = 'yes'
                            hold = student.name
                            print("ACCOUNT HOLDER : ", hold)
                            print("_____L_O_A_D_I_N_G_______\n")
                            student_object = student
                            break
                    if list_students.index(student) == len(list_students) - 1:
                        if found == 'no':
                            print("Student Doesn't exist")
                            return "Please create User first!"
        else:
            for item in _active_users:
                try:
                    if student_object.name in item:
                        print("User session already active!")
                        return student_object.name + ":" + "active"
                except AttributeError:
                    list_students = InnitializeStudents.all()

                    for student in list_students:
                        if student_object in student.name:
                            if student.name in _active_users:
                                print("User session already active!")
                                return student.name + ":" + "active"
                        if list_students.index(student) == len(list_students) - 1:
                            print("Student Doesn't exist")
                            return "Please create User first!"
        if len(password) < 8:
            print("Password should be atleast 8 characters!!")
            return
        else:
            try:
                file = open("sessionsDB", "r+")
                temp = file.readlines()
                temp = Lists.strip_from_items(temp,"\n")
                if temp == []:
                    print("Creating new User session...")
                    writeline = student_object.name + "$" + password + "\n"
                    file.close()
                    file = open("sessionsDB", "a")
                    file.writelines(writeline)
                    file.close()
                    print("User created... loging in...")
                    print("Welcome", student_object.name)
                    _active_users.append(student_object.name)
                    return _active_users
            except:
                file = open("sessionsDB", "w+")
                temp = file.readlines()
                temp = Lists.strip_from_items(temp, "\n")
                if temp == []:
                    print("Creating new User session...")
                    writeline = student_object.name + "$" + password + "\n"
                    file.close()
                    file = open("sessionsDB", "a")
                    file.writelines(writeline)
                    file.close()
                    print("User created... loging in...")
                    print("Welcome", student_object.name)
                    _active_users.append(student_object.name)
                    return _active_users

            for item in temp:
                if student_object.name in item:
                    print("Attempting to log in")
                    hold = item.split("$",1)
                    if password == hold[1]:
                        print("Login success")
                        print("Welcome", student_object.name)
                        _active_users.append(student_object.name)
                        return _active_users
                    else:
                        print("Invalid Password for", student_object.name)
                        return student_object.name + ":" + "inactive"
                elif temp.index(item) + 1 == len(temp):
                    print("Creating new User session...")
                    writeline = student_object.name + "$" + password + "\n"
                    file.close()
                    file = open("sessionsDB", "a")
                    file.writelines(writeline)
                    file.close()
                    print("User created... loging in...")
                    print("Welcome", student_object.name)
                    _active_users.append(student_object.name)
                    return _active_users

    def get_active_users(active_list):
        admin = input("Enter the Admin username : ")
        password = input("Enter the password : ")

        if admin != 'admin' and password != 'admin':
            print("Error...Invalid Admin")
            return "error"

        print("Fetching active users...")
        return active_list

    def log_out(student_object,active_list):
        active_users = active_list
        for item in active_users:
            if student_object.name in item:
                active_users.remove(student_object.name)
                print("Logged out", student_object.name)
                return student_object.name + ":" + "inactive"
        print("No such session")

    def get_all_sessions():
        file = open("sessionsDB", "r+")
        temp = file.readlines()
        temp = Lists.strip_from_items(temp, "\n")
        file.close()
        return temp
