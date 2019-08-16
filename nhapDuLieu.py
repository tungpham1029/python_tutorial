def tieude():
    f = open("duLieu.txt", 'a', encoding='utf-8')
    f.write('So Thu Tu, Ho Ten, Dia Chi: \n')

def luuFile(s):
    f = open("duLieu.txt",'a',encoding='utf-8')
    f.writelines(s+'\n')
    print()

def nhapFile():
    stt = int(input("Nhap so thu tu: "))
    ten = input("Nhap ho ten: ")
    diachi = input("Nhap dia chi hoc sinh: ")
    s = str(stt) +','+ten+','+diachi
    luuFile(s)

def main():
    tieude()
    while True:
        nhapFile()
        print("nhap Y de tiep tuc, N de thoat ")
        k = input("nhap [Y/N]: ")
        if k == 'Y' or k == 'y':
            continue
        elif k == 'N' or k == 'n':
            exit()
main()