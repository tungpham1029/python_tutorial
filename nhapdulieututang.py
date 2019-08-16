def nhapDuLieu():
    f = open('nhapDuLieu.txt','a',encoding='utf-8')
    f.writelines('So Thu Tu, Ho Ten, Dia Chi:\n')
    stt = 0
    while True:
        stt += 1
        ten = input("Nhap ho ten: ")
        diachi = input("Nhap dia chi hoc sinh: ")
        s = str(stt) + ',' + ten + ',' + diachi
        f.writelines(s + '\n')
        print("nhap ")
        k = input("nhap [Y/N]: ")
        if k == 'Y':
            continue
        elif k == 'N':
            exit()
        else:
            print("Phai phai chon Y hoac N: ")
            print("Chon Y de tiep tuc, N de thoat")
            k = input("nhap [Y/N]: ")
    f.close()
nhapDuLieu()