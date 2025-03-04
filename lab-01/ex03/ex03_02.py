def dao_nguoc_list(lst):
    return lst[::-1]

# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# Đảo ngược danh sách
list_dao_nguoc = dao_nguoc_list(numbers)

# Hiển thị kết quả
print("List sau khi đảo ngược:", list_dao_nguoc)
