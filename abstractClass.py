import numpy as np
from abc import ABC, abstractclassmethod


class People(ABC):

    @abstractclassmethod
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    @abstractclassmethod
    def add(self):
        pass
    @abstractclassmethod
    def showList(self):
        pass
    @abstractclassmethod
    def showNameWithCLassroom(self):
        pass
    @abstractclassmethod
    def edit(self):
        pass
    @abstractclassmethod
    def delete(self):
        pass

class Student(People):
    def __init__(self, id, name, address, learned_classroom):
        super().__init__(id, name, address)
        self.learned_classroom = learned_classroom

    def add(self):
        print("Before Add Student")
        self.showList()
        f = open('filestudent.txt', 'a', encoding="utf-8")
        self.id = int(input("Input id: "))
        self.name = input("Input name: ")
        self.address = input("Input address: ")
        self.learned_classroom  = input("Input learned classroom: ")
        line = str(self.id) +','+ self.name + ',' + self.address +','+ self.learned_classroom+'\n'
        f.writelines(line)
        f.close()
        print("After Add Student")
        self.showList()

    def showList(self):
        lines = []
        f = open('filestudent.txt', 'r', encoding='utf-8')
        for line in f:
            data = line.strip()
            lines.append(data.split(","))
        for row in lines:
            for element in row:
                print(element, end=' ')
            print()
        print()
        f.close()

    def showNameWithCLassroom(self):
        listStudent = []
        lines = []
        f = open('filestudent.txt', 'r', encoding= 'utf-8')
        for line in f:
            data = line.strip(",")
            listStudent.append(data.split(","))
        print("List All Student ")
        self.showList()
        print("Show name with classroom")
        name = input("input name: ")
        for i in range(len(listStudent)):
            if listStudent[i][1] == name:
                lines.append('Name '+listStudent[i][1]+" with Id "+listStudent[i][0]+\
                             ' is learning in classroom '+listStudent[i][3])
        print("".join(lines))
        f.close()

        # lines = f.readlines()
        # print(lines)
        # print("Student is learning in room: ")
        # name = input("Input name: ")
        # for i in range(len(lines)):
        #     print(lines[i][2])
        #     if lines[i][2] == name:
        #         print(lines[i][1])
        #         result.append(lines[i][1])
        #         result.append(lines[i][3])
        # print(result)

    def edit(self):
        listStudent = []
        f = open('filestudent.txt','r', encoding='utf-8')
        for line in f:
            data = line.strip(",")
            listStudent.append(data.split(","))
        print("Before Edit")
        self.showList()
        Id = int(input("Input Id want to change information: "))
        for i in range(len(listStudent)):
            if int(listStudent[i][0]) == Id:
                listStudent[i][1] = input("Edit name: ")
                listStudent[i][2] = input("Edit address: ")
                listStudent[i][3] = input("Edit class room: ")
                # self.name = input("Edit name: ")
                # self.address = input("Edit address: ")
                # self.learned_classroom = input("Edit class room: ")
        k = 0
        lines = ''
        while k < len(listStudent):
            line = ','.join(listStudent[k]).strip("\n")
            print(line)
            k+=1
            lines  += line+'\n'
        f = open("filestudent.txt",'w')
        f.writelines(lines)
        f.close()
        print("After Edit: ")
        self.showList()
        # f = open("filestudent.txt", 'w')
        # f.writelines(",".join(listStudent))
        # f.close()

        # lines = f.readlines()
        # print("Id need to be Edit: ")
        # Id = int(input("Input Id: "))
        # for i in range(len(lines)):
        #     if int(lines[i][0])== Id:
        #         self.name = input("Edit name: ")
        #         self.address = input("Edit address: ")
        #         self.learned_classroom = input("Edit class room: ")
        #         lines[i] = str(i+1) +','+ self.name +','+ self.address +','+ self.learned_classroom
        # f = open("filestudent.txt", 'w')
        # f.writelines(lines)
        # f.close()

    def delete(self):
        listStudent = []
        f = open("filestudent.txt", 'r')
        for line in f:
            data = line.strip(",")
            listStudent.append(data.split(","))
        print("Before Delete: ")
        self.showList()
        Id = int(input("Input Id want to be Delete: "))

        k = 0
        while k < len(listStudent):
            if int(listStudent[k][0])== Id:
                listStudent.remove(listStudent[k])
            k += 1
            # print("result")
            # print(result)
            # print("result")
        # print(listStudent)
        # lines = ''
        #
        i = 0
        lines = ''
        while i < len(listStudent):
            line = ','.join(listStudent[i]).strip("\n")
            print(line)
            i += 1
            lines += line + '\n'
        f = open("filestudent.txt", 'w')
        f.writelines(lines)
        f.close()
        print("After Delete: \n")
        self.showList()



        # lines = f.readlines()
        # print("Id need to be Delete: ")
        # Id = int(input("Input Id: "))
        # k = 0
        # while k<len(lines):
        #     if int(lines[k][0])== Id:
        #         lines.remove(lines[k])
        #     k+=1
        # f = open('filestudent.txt','w')
        # f.writelines(lines)
        # f.close()

class Teacher(People):
    def __init__(self, id, name, address, teached_classroom):
        super().__init__(id, name, address)
        self.teached_classroom = teached_classroom

    def add(self):
        print("Before Add teacher")
        self.showList()
        f = open('fileteacher.txt', 'a', encoding="utf-8")
        self.id = int(input("Input id: "))
        self.name = input("Input name: ")
        self.address = input("Input address: ")
        self.teached_classroom  = input("Input teached classroom: ")
        line = str(self.id) +','+ self.name + ',' + self.address +','+ self.teached_classroom+'\n'
        f.writelines(line)
        f.close()
        print("After Add Teach")
        self.showList()

    def showList(self):
        lines = []
        f = open('fileteacher.txt', 'r', encoding='utf-8')
        for line in f:
            data = line.strip()
            lines.append(data.split(","))
        for row in lines:
            for element in row:
                print(element, end=' ')
            print()
        print()
        f.close()

    def showNameWithCLassroom(self):
        listTeacher = []
        lines = []
        f = open('fileteacher.txt', 'r', encoding= 'utf-8')
        for line in f:
            data = line.strip(",")
            listTeacher.append(data.split(","))
        print("List All Student ")
        self.showList()
        print("Show name with classroom")
        name = input("input name: ")
        for i in range(len(listTeacher)):
            if listTeacher[i][1] == name:
                lines.append('Name '+listTeacher[i][1]+" with Id "+listTeacher[i][0]+\
                             ' is learning in classroom '+listTeacher[i][3])
        print("".join(lines))
        f.close()

    def edit(self):
        listTeacher = []
        f = open('fileteacher.txt','r', encoding='utf-8')
        for line in f:
            data = line.strip(",")
            listTeacher.append(data.split(","))
        print("Before Edit")
        self.showList()
        Id = int(input("Input Id want to change information: "))
        for i in range(len(listTeacher)):
            if int(listTeacher[i][0]) == Id:
                listTeacher[i][1] = input("Edit name: ")
                listTeacher[i][2] = input("Edit address: ")
                listTeacher[i][3] = input("Edit class room: ")
        k = 0
        lines = ''
        while k < len(listTeacher):
            line = ','.join(listTeacher[k]).strip("\n")
            print(line)
            k+=1
            lines  += line+'\n'
        f = open("fileteacher.txt",'w')
        f.writelines(lines)
        f.close()
        print("After Edit: ")
        self.showList()

    def delete(self):
        listTeacher = []
        f = open("fileteacher.txt", 'r')
        for line in f:
            data = line.strip(",")
            listTeacher.append(data.split(","))
        print("Before Delete: ")
        self.showList()
        Id = int(input("Input Id want to be Delete: "))

        k = 0
        while k < len(listTeacher):
            if int(listTeacher[k][0]) == Id:
                listTeacher.remove(listTeacher[k])
            k += 1

        i = 0
        lines = ''
        while i < len(listTeacher):
            line = ','.join(listTeacher[i]).strip("\n")
            print(line)
            i += 1
            lines += line + '\n'
        f = open("fileteacher.txt", 'w')
        f.writelines(lines)
        f.close()
        print("After Delete: \n")
        self.showList()


class Main():
    while True:
        print("1. Student Management !")
        print("2. Teacher Management !")
        print("3. Exit")
        k = int(input("Input Number: "))
        if k == 1:
            student = Student("id","name","address","classroom")
            while True:
                print("1. Add Student \n"
                      "2. Show Student \n"
                      "3. Show Student with Classroom\n"
                      "4. Edit Student \n"
                      "5. Delete Student \n"
                      "6. Back Main")
                num = int(input("Input Number: "))
                if num == 1:
                    student.add()
                elif num == 2:
                    student.showList()
                elif num == 3:
                    student.showNameWithCLassroom()
                elif num == 4:
                    student.edit()
                elif num == 5:
                    student.delete()
                elif num == 6:
                    break

        elif k == 2:
            teacher = Teacher("id", "name", "address", "classroom")
            while True:
                print("1. Add Teacher \n"
                      "2. Show Teacher \n"
                      "3. Show Teacher with Classroom\n"
                      "4. Edit Teacher \n"
                      "5. Delete Teacher \n"
                      "6. Back Main")
                num = int(input("Input Number: "))
                if num == 1:
                    teacher.add()
                elif num == 2:
                    teacher.showList()
                elif num == 3:
                    teacher.showNameWithCLassroom()
                elif num == 4:
                    teacher.edit()
                elif num == 5:
                    teacher.delete()
                elif num == 6:
                    break
        elif k == 3:
            exit()
Main()