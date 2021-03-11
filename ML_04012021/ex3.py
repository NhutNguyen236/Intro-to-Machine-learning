import numpy as np

a = np.zeros((3,2))
print(a)

b = np.ones((1,2))
print('\n', b)

c = np.full((3,4),7)
print('\n', c)

d = np.eye(4)
print('\n', d)

e = np.random.random((4,3))
print('\n',e)

print("=============================")

L = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
print(L[:2, 1:3])

print(L[:1,2])

row_r1 = L[1:2, :]
print('row:',row_r1)
print('row_shape', row_r1.shape)
