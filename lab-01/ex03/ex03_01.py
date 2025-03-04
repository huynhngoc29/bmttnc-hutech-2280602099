def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Nhập danh sách số từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# Tính tổng các số chẵn
tong_chan = tinh_tong_so_chan(numbers)

# Hiển thị kết quả
print("Tổng các số chẵn trong list là:", tong_chan)
