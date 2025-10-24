import numpy as np
# 1. Tạo mảng và truy cập
a=np.arange(3)
print(" Mảng a:\n", a)
a1=np.arange(12).reshape(3,4)
print(" Mảng a1 (reshape 3x4):\n", a1)

b=np.ones((1,2))
print("mảng b (matrix 1x2 toàn 1):\n", b)

c=np.full((3,2,2),9)
print("mảng c (matrix 3x2x2 toàn 9):\n", c)

d=np.eye(3)
print("mảng d (ma trận đơn vị 3x3): \n", d)

#Ma trận ngẫu nhiên 3x3
M_rand = np.random.randint(1, 10, size=(3, 3))
print(" Ma trận ngẫu nhiên:\n", M_rand)

# Ma trận vuông với đường chéo chính 1,2,3
M_diag = np.diag([1, 2, 3])
print(" Ma trận đường chéo:\n", M_diag)

