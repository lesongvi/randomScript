import random

tran=1
tong=10
hoa=0
thang=0
thua=0
print("======================================================")
print(" ")
print("Chào mừng mấy thằng gay đến với game oẳn tù xì.\n")
print(f"Điểm số hiện tại là {tong}")
print(" Sẵn sàng để chơi với máy tính.\n")
while tran<=tong:
    comp =["B","N","K"]
    comp_ans= random.choice(comp)
    print("Nhập [ B là Búa ][ N là bao Ni-lông ][ K là Kéo]")
    ans = input("==> ")
    ans = ans.upper()
    if(ans=='B'):
        print("Bạn chọn: Búa")
        if (ans=='B' and comp_ans=='K'):
            print(f"Máy chọn Kéo\n")
            print("======  BẠN THẮNG  ======")
            thang+=1
        elif(ans=='B' and comp_ans=='B'):
            print(f"Máy chọn Búa\n")
            print("======  HÒA  ======")
            hoa+=1
        elif(ans=='B' and comp_ans=='N'):
            print(f"Máy chọn Bao\n")
            print("======  BẠN THUA  ======")
            thua+=1

    elif(ans=='N'):
        print("Bạn chọn: Giấy")
        if (ans=='N' and comp_ans=='K'):
            print(f"Máy chọn Kéo\n")
            print("======  BẠN THUA  ======")
            thua+=1
        elif(ans=='N' and comp_ans=='B'):
            print(f"Máy chọn Búa\n")
            print("======  BẠN THẮNG  ======")
            thang+=1
        elif(ans=='N' and comp_ans=='G'):
            print(f"Máy chọn Bao\n")
            print("======  HÒA  ======")
            hoa+=1

    elif(ans=='K'):
        print("Bạn chọn: Kéo")
        if (ans=='K' and comp_ans=='K'):
            print(f"Máy chọn Kéo\n")
            print("======  HÒA  ======")
            hoa+=1
        elif(ans=='K' and comp_ans=='B'):
            print(f"Máy chọn Búa\n")
            print("======  BẠN THUA  ======")
            thua+=1
        elif(ans=='K' and comp_ans=='N'):
            print(f"Máy chọn Bao\n")
            print("======  BẠN THẮNG  ======")
            thang+=1
    else:
        print("Nhập sai nhập lại")
        tran-=1
    print(f"Trận #{tran}")
    print("-------------------------------------------")
    tran+=1

print(f""" 
        Số trận:   {tong}
            Thắng:   {thang}
           Thua:   {thua}
           Hòa:   {hoa}""")
