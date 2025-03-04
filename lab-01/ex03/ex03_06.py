def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

# Tạo Dictionary mẫu
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Nhập khóa cần xóa
key_to_delete = 'b'

# Gọi hàm xóa phần tử
result = xoa_phan_tu(my_dict, key_to_delete)

# Kiểm tra kết quả
if result:
    print("Phần tử đã được xóa khỏi Dictionary:", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")
