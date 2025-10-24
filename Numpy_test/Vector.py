import numpy as np
v1=np.array([1, 2, 3])
v2=np.array([4, 5, 6])

# 1.Cộng hai vector
v_sum = v1 + v2
print("Cộng hai vector:", v_sum)

# 2.Trừ hai vector
v_diff = v1 - v2
print("Trừ hai vector:", v_diff)

# 3.Nhân vô hướng
scalar = 3
v_scalar_mult = v1 * scalar
print("Nhân vô hướng:", v_scalar_mult)

# 4.Tích vô hướng
dot_product = np.dot(v1, v2)
print("Tích vô hướng:", dot_product)

# 5.Độ dài của vector
magnitude = np.linalg.norm(v1)
print("Độ dài của vector v1:", magnitude)

# 6.Chuẩn hóa vector
v_norm = v1 / np.linalg.norm(v1)
print("Chuẩn hóa vector:", v_norm)

# 7.Tính góc giữa hai vector (bằng radian)
cos_theta = dot_product / (np.linalg.norm(v1) * np.linalg.norm(v2))
angle = np.arccos(cos_theta)
print("Góc giữa hai vector (radian):", angle)

# 8/Tích có hướng (cross product)
v_cross = np.cross(v1, v2)
print("Tích có hướng:", v_cross)

# 9. Vector chuyển vị (1D thì giống nhau)
v_trans = v1.T
print(" Chuyển vị vector:", v_trans)

v_mul = v1 * v2
print(" Nhân từng phần tử:", v_mul)

# 10. Ghép vector (nối)
v_concat = np.concatenate((v1, v2))
print(" Nối vector:", v_concat)

# 11. Vector cộng hằng số
v_plus_const = v1 + 5
print("8. Cộng hằng số:", v_plus_const)

# 12. Vector ngẫu nhiên
v_rand = np.random.randint(1, 10, size=5)
print("7. Vector ngẫu nhiên:", v_rand)