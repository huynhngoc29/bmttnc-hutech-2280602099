def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

# Nhập tuple từ người dùng
input_tuple = eval(input("Nhập tuple (ví dụ: (1, 2, 3, 4)): "))

# Lấy phần tử đầu và cuối
first, last = truy_cap_phan_tu(input_tuple)

# Hiển thị kết quả
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)
