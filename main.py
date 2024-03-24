import numpy as np
a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)