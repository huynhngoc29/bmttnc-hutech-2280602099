def daonguocchuoi(chuoi):
    return chuoi[:: -1]

input_string = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ", daonguocchuoi(input_string))