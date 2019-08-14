import math

def giaipt(a,b,c):
    if a == 0:
        print("gia tri cua a phai khac 0")
        pass
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("phuong trinh vo nghiem")
        elif delta == 0:
            x = -b/(2*a)
            print("phuong trinh co nghiem kep: x1 = x2 = ",x)
        else:
            x1 = (-b-math.sqrt(delta))/(2*a)
            x2 = (-b+math.sqrt(delta))/(2*a)
            print("phuong trinh co 2 nghiem phan biet: ")
            print("x1 = ",x1, "\nx2 = ",x2)

def main():
    print("Giai phuong trinh bac 2: a.x^2 + b.x+ c = 0")
    print("nhap gia tri a, b, c: ")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        giaipt(a, b, c)
    except ValueError:
        print("Ban Phai Nhap So Thuc")
        print()

while True:
    main()
    print()
    print("Chon Y de tiep tuc, N de thoat")
    k = input("Moi ban chon: [Y/N]")
    if k == 'Y' or k =='y':
        continue
    elif k == 'N' or k == 'n':
        exit()
    else:
        print()
        print("Phai phai chon Y hoac N: ")
        print("Chon Y de tiep tuc, N de thoat")
        k = input("Moi ban chon: [Y/N]")

