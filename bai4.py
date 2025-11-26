while True:
    print("\nMay tinh mini:%")
    print("1. Cong")
    print("2. Tru")
    print("3. Nhan")
    print("4. Chia")
    print("5. Thoat")
    
    choose = input("Chon (1-5): ")
    if choose == '5':
        break
    else:
        print("Nhap hai so (cach nhau boi dau phay): ", end="")
        a, b = map(int, input().split(','))
        match choose:
            case '1':
                print(f"Ket qua: {a} + {b} = {a + b}")
            case '2':
                print(f"Ket qua: {a} - {b} = {a - b}")
            case '3':
                print(f"Ket qua: {a} * {b} = {a * b}")
            case '4':
                if b == 0:
                    print("Loi: Khong the chia cho 0")
                else:
                    print(f"Ket qua: {a} / {b} = {a / b}")
            case _:
                print("Lua chon khong hop le (1 - 5)")