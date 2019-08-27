from abc import ABC, abstractclassmethod

class People(ABC):

    @abstractclassmethod
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    @abstractclassmethod
    def add(self, id, name, address):
        self.id = int(input("Input id: "))
        self.name = input("Input name: ")
        self.address = input("Input address: ")
        self.line = str(self.id) +','+ self.name +','+self.address

    @abstractclassmethod
    def show_list(self, path):
        f = open(path, 'r', encoding='utf-8')
        lines = []
        for line in f:
            data = line.strip()
            lines.append(data.split(","))
        for row in lines:
            for element in row:
                print(element, end=' ')
            print()
        print()
        f.close()

    @abstractclassmethod
    def name_with_classroom(self, path):
        f = open(path, 'r', encoding='utf-8')
        lis = []
        lines = []
        for line in f:
            data = line.strip(",")
            lis.append(data.split(","))
        print("Show name with classroom")
        name = input("input name: ")
        for i in range(len(lis)):
            if lis[i][1] == name:
                lines.append('Name ' + lis[i][1] + " with Id " + lis[i][0] + \
                             ' is in classroom ' + lis[i][3])
        print("".join(lines))
        f.close()

    @abstractclassmethod
    def edit(self, path):
        f = open(path, 'r', encoding='utf-8')
        lis = []
        for line in f:
            data = line.strip(",")
            lis.append(data.split(","))
        Id = int(input("Input Id want to change information: "))
        for i in range(len(lis)):
            if int(lis[i][0]) == Id:
                lis[i][1] = input("Edit name: ")
                lis[i][2] = input("Edit address: ")
                lis[i][3] = input("Edit class room: ")

        k = 0
        lines = ''
        while k < len(lis):
            line = ','.join(lis[k]).strip("\n")
            k += 1
            lines += line + '\n'
        f = open(path, 'w', encoding='utf-8')
        f.writelines(lines)
        f.close()

    @abstractclassmethod
    def delete(self, path):
        lis = []
        f = open(path, 'r', encoding='utf-8')
        for line in f:
            data = line.strip(",")
            lis.append(data.split(","))
        Id = int(input("Input Id want to be Delete: "))

        k = 0
        while k < len(lis):
            if int(lis[k][0]) == Id:
                lis.remove(lis[k])
            k += 1

        i = 0
        lines = ''
        while i < len(lis):
            line = ','.join(lis[i]).strip("\n")
            lines += line + '\n'
            i += 1
        f = open(path, 'w', encoding='utf-8')
        f.writelines(lines)
        f.close()

class Student(People):

    def __init__(self, id, name, address, learned_classroom):
        super().__init__(id, name, address)
        self.learned_classroom = learned_classroom

    def add(self, id, name, address):
        path = 'filestudents.txt'
        f = open(path, 'a', encoding="utf-8")
        self.show_list(path)
        super().add(id, name, address)
        self.learned_classroom  = input("Input learned classroom: ")
        # line = str(self.id) +','+ self.name + ',' + self.address +','+ self.learned_classroom+'\n'
        line = self.line + ',' + self.learned_classroom + '\n'
        f.writelines(line)
        f.close()

    def show_list(self, path):
        super().show_list(path)

    def name_with_classroom(self, path):
        self.show_list(path)
        super().name_with_classroom(path)

    def edit(self, path):
        self.show_list(path)
        super().edit(path)
        self.show_list(path)

    def delete(self, path):
        self.show_list(path)
        super().delete(path)
        self.show_list(path)

class Teacher(People):

    def __init__(self, id, name, address, teached_classroom):
        super().__init__(id, name, address)
        self.teached_classroom = teached_classroom

    def add(self, id, name, address):
        path = 'fileteachers.txt'
        f = open(path, 'a', encoding="utf-8")
        self.show_list(path)
        super().add(id, name, address)
        self.teached_classroom  = input("Input teached classroom: ")
        # line = str(self.id) +','+ self.name + ',' + self.address +','+ self.learned_classroom+'\n'
        line = self.line + ',' + self.teached_classroom + '\n'
        f.writelines(line)
        f.close()

    def show_list(self, path):
        super().show_list(path)

    def name_with_classroom(self, path):
        self.show_list(path)
        super().name_with_classroom(path)

    def edit(self, path):
        self.show_list(path)
        super().edit(path)
        self.show_list(path)

    def delete(self, path):
        self.show_list(path)
        super().delete(path)
        self.show_list(path)


class Main():
    while True:
        print("1. Student Management !")
        print("2. Teacher Management !")
        print("3. Exit")
        k = int(input("Input Number: "))
        if k == 1:
            path = 'filestudents.txt'
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
                    student.add("id", "name","address")
                elif num == 2:
                    student.show_list(path)
                elif num == 3:
                    student.name_with_classroom(path)
                elif num == 4:
                    student.edit(path)
                elif num == 5:
                    student.delete(path)
                elif num == 6:
                    break

        elif k == 2:
            path = 'fileteachers.txt'
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
                    teacher.add('id', 'name', 'address')
                elif num == 2:
                    teacher.show_list(path)
                elif num == 3:
                    teacher.name_with_classroom(path)
                elif num == 4:
                    teacher.edit(path)
                elif num == 5:
                    teacher.delete(path)
                elif num == 6:
                    break
        elif k == 3:
            exit()
Main()