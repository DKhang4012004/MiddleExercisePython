import numpy as np

v1=np.random.randint(1,10,size=(3,3))
v2=np.random.randint(1,10,size=(3,3))

print(" Ma trận v1:\n", v1)
print(" Ma trận v2:\n", v2)

# 1.Cộng hai ma trận
sum_matrix = v1 + v2
print(" Ma trận tổng (v1 + v2):\n", sum_matrix)

# 2.Nhân hai ma trận
product_matrix = np.dot(v1, v2)
print(" Ma trận tích (v1 * v2):\n", product_matrix)

# 3.Chuyển vị ma trận v1
transpose_v1 = v1.T
print(" Ma trận chuyển vị của v1:\n", transpose_v1)

# 4.Tính định thức của ma trận v1
det_v1 = np.linalg.det(v1)
print(" Định thức của ma trận v1:", det_v1)

# 5.Tính ma trận nghịch đảo của v1 (nếu khả thi)
if det_v1 != 0:
    inverse_v1 = np.linalg.inv(v1)
    print(" Ma trận nghịch đảo của v1:\n", inverse_v1)
else:
    print(" Ma trận v1 không khả nghịch (định thức bằng 0).")

# 6.Nối mảng
concat_matrix = np.concatenate((v1, v2), axis=0)
print(" Ma trận nối v1 và v2 theo hàng:\n", concat_matrix)

# 7.Trích xuất dữ liệu
#lọc phần tử theo chỉ số
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array([0,2,0,1])
print("Danh sach chi muc: \n ",a[np.arange(4),b])

a[np.arange(4),b] +=10
print("Sau khi tang gia tri: \n", a)

#lọc phần tử theo điều kiện
print("Phan tu lon hon 2 trong a la: ", a[a>2])

#trich hang 2 cot 1
print("Trich hang 2 cot 1 trong a: \n", a[2:3,1:2])


# 8.Thay đổi hình dạng mảng
reshaped_a = a.reshape(3, 4)
print(" Ma trận v1 sau khi thay đổi hình dạng (reshape 1x9):\n", reshaped_a)
print("kich thuoc cua reshaped_a: ", reshaped_a.shape)
print("kich thuoc cua a: ", a.shape)

# 9.Tính toán thống kê
mean_v1 = np.mean(v1)
sum_v1 = np.sum(v1)
max_v1 = np.max(v1)
Sum_col_v1 = np.sum(v1, axis=0)
print(" Tong cac cot trong v1: ", Sum_col_v1)
print(" Giá trị trung bình của v1:", mean_v1)
print(" Tổng các phần tử của v1:", sum_v1)
print(" Giá trị lớn nhất trong v1:", max_v1)

#10. hstack,vstack
hstack_matrix = np.hstack((v1, v2))
print(" Ma trận sau khi hstack v1 và v2:\n", hstack_matrix)
vstack_matrix = np.vstack((v1, v2))
print(" Ma trận sau khi vstack v1 và v2:\n", vstack_matrix)

#11. Sắp xếp ma trận
sorted_v1 = np.sort(v1, axis=0)
print(" Ma trận v1 sau khi sắp xếp theo cột:\n", sorted_v1)
print(" Ma trận v1 sau khi sắp xếp theo hàng:\n", np.sort(v1, axis=1))






