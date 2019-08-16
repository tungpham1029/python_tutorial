def nhapDuLieu():
    f = open('nhapDuLieu.txt','a',encoding='utf-8')
    f.writelines('So Thu Tu, Ho Ten, Dia Chi:\n')
    while True:
        stt = int(input("Nhap so thu tu: "))
        ten = input("Nhap ho ten: ")
        diachi = input("Nhap dia chi hoc sinh: ")
        s = str(stt) + ',' + ten + ',' + diachi
        f.writelines(s + '\n')
        print("nhap Y de tiep tuc, N de thoat")
        k = input("nhap [Y/N]: ")
        if k == 'Y' or k == 'y':
            continue
        elif k == 'N' or k =='n':
            exit()
    f.close()
nhapDuLieu()