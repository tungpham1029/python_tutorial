path = "liststudent.txt"

def AddStudent():
    f = open(path, 'a', encoding='utf-8')
    Id = int(input("Input Id: "))
    Name = input("Input Name: ")
    Year = int(input("Input Year: "))
    line = str(Id) + ',' + Name + ','+ str(Year)
    f.writelines(line+'\n')
    f.close()

def ShowListStudent():
    lines = []
    f = open(path, 'r', encoding='utf-8')
    for line in f:
        data = line.strip()
        lines.append(data.split(","))
    for row in lines:
        for element in row:
            print(element, end =' ')
        print()
    print()
    f.close()

def UpdateStudent():
    print("File before Update")
    ShowListStudent()
    f = open(path, 'r')
    lines = f.readlines()
    print(lines)
    IdNeedToEdit = int(input("ID Need To Edit: "))
    for i in range(len(lines)):
        if int(lines[i][0]) == IdNeedToEdit:
            name = input("new name: ")
            year = int(input("new year: "))
            lines[i] = str(i+1) + "," + name + "," + str(year) + '\n'
            print(lines)
    f = open(path, 'w')
    f.writelines(lines)
    f.close()
    ShowListStudent()
    # UpdateId = int(input("Input Id need to update: "))
    # for i in range(len(lines)):
    #     if int(lines[i][0])==UpdateId:
    #         Id = int(input("Input Id: "))
        #     Name = input("Input Name: ")
        #     Year = int(input("Input Year: "))
        #     lines[i] = [Id, Name, Year]
        # print(lines)
        # line = lines[0]= str(Id)+','+Name+',' +str(Year)+'\n'
    # if int(lines[1][0])==UpdateId:
    #     Id = int(input("Input Id: "))
    #     Name = input("Input Name: ")
    #     Year = int(input("Input Year: "))
    #     line = lines[0]= str(Id)+','+Name+',' +str(Year)
    #     f.writelines(line)
    #     ShowFile()

        # for row in lines:
        #     for element in row:
        #         print(element, end=' ')
        #     print()
        # print()
def DeleteStudent():
    print("File before Delete")
    ShowListStudent()
    f = open(path, 'r')
    lines = f.readlines()
    print(type(lines))
    print(lines)
    IdNeedToDelete = int(input("ID Need To Delete: "))
    k=0
    while k<len(lines):
        print(k)
        if int(lines[k][0]) == IdNeedToDelete:
            lines.remove(lines[k])
        k+=1
    f = open(path, 'w')
    f.writelines(lines)
    f.close()
    ShowListStudent()
    # for i in range(k):
    #     if int(lines[i][0]) == IdNeedToDelete:
    #         lines.remove(lines[i])
    #     k-=1
    # f = open(path, 'w')
    # f.writelines(lines)
# AddSv()
# UpdateFile()
# ShowFile()
# DeleteSv()
def Main():
    while True:
        print("Press 1: Add Student !")
        print("Press 2: Show Student !")
        print("Press 3: Edit Student !")
        print("Press 4: Delete Student !")
        print("Press 5: Exit !")
        number = int(input("Press: "))
        if number == 1:
            AddStudent()
        elif number == 2:
            ShowListStudent()
        elif number == 3:
            UpdateStudent()
        elif number == 4:
            DeleteStudent()
        elif number == 5:
            exit()

Main()

# switcher={
#     1: AddSv(),
#     2: ShowFile(),
#     3: UpdateFile(),
#     4: DeleteSv()
# }

