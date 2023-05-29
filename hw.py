import numpy as np


# 1
first_10_int = np.arange(1, 11)
print(f"{first_10_int=}")

# 2
zero = np.zeros((3, 3), dtype=int)
print(f"{zero=}")


#3
random_matrix_1_10 = np.random.randint(1, 11, (5, 5))
print(f"{random_matrix_1_10=}")


#4
random_0_1 = np.random.rand(4, 4)
print(f"{random_0_1=}")


#5
matrix_1 = np.random.randint(1, 11, (5,))
matrix_2 = np.random.randint(1, 11, (5,))
matrix_sum = matrix_1 + matrix_2
print(f"{matrix_sum=}")
matrix_sub = matrix_1 - matrix_2
print(f"{matrix_sub=}")
matrix_mul = matrix_1 * matrix_2
print(f"{matrix_mul=}")


#6
vector1 = np.random.randint(1, 20 , (7,))
vector2 = np.random.randint(1, 20 , (7,))
scalar = np.dot(vector1, vector2)
print(f"{scalar=}")


#7
matrix_2_2 = np.random.randint(1, 11, (2, 2))
matrix_2_3 = np.random.randint(1, 11, (2, 3))
mul_matrix_2_2_matrix_2_3 = np.dot(matrix_2_2, matrix_2_3)
print(f"{mul_matrix_2_2_matrix_2_3=}")


#8
matrix_3_3 = np.random.randint(1, 11, (3, 3))
matrix_3_3_inv = np.linalg.inv(matrix_3_3)
print(f"{matrix_3_3_inv=}")


#9
matrix_4_4 = np.random.random((4, 4))
print(f"{matrix_4_4=}")
print(f"{matrix_4_4.T=}")


#10
matrix_3_4 = np.random.randint(1, 11, (3, 4))
vector_4 = np.random.randint(1, 11, (4,))
mul_matrix_3_4_vector_4 = np.dot(matrix_3_4, vector_4)
print(f"{mul_matrix_3_4_vector_4=}")


#11
matrix_2_3 = np.random.random((2, 3))
vector_3 = np.random.random((4,))
mul_matrix_2_3_vector_3 = np.dot(matrix_3_4, vector_4)
print(f"{mul_matrix_2_3_vector_3=}")


#12
matrix_2_2_1 = np.random.randint(1, 11, (2, 2))
matrix_2_2_2 = np.random.randint(1, 11, (2, 2))
mul_matrix_2_2_1_matrix_2_2_2 = matrix_2_2_1 * matrix_2_2_2
print(f"{mul_matrix_2_2_1_matrix_2_2_2=}")


#13
matrix_2_2_1 = np.random.randint(1, 11, (2, 2))
matrix_2_2_2 = np.random.randint(1, 11, (2, 2))
mul_matrix_2_2_1_matrix_2_2_2 = np.dot(matrix_2_2_1, matrix_2_2_2)
print(f"{mul_matrix_2_2_1_matrix_2_2_2=}")


#14
matrix_5_5 = np.random.randint(1, 101, (5, 5))
print(f"{matrix_5_5.sum()=}")


#15
matrix_4_4_1 = np.random.randint(1, 11, (4, 4))
matrix_4_4_2 = np.random.randint(1, 11, (4, 4))
sub_matrix_4_4_1_matrix_4_4_2 = matrix_4_4_1 - matrix_4_4_2
print(f"{sub_matrix_4_4_1_matrix_4_4_2=}")


#16
matrix_3_3 = np.random.random((3, 3))
matix_1_3 = np.array(
    [[matrix_3_3[0].sum()], [matrix_3_3[1].sum()], [matrix_3_3[2].sum()]])
print(f"{matix_1_3=}")


#17
matrix_3_4 = np.random.randint(1, 11, (3, 4))
print(f"{matrix_3_4=}")
print(f"{matrix_3_4*matrix_3_4=}")


#18
vector_4 = np.random.randint(1, 51, (4,))
vector_4_sqrt = np.sqrt(vector_4)
print(f"{vector_4_sqrt=}")
