import np
import numpy as np
a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)

print("\n\n")
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

print("\n\n")
m = np.array((np.arange(2), np.arange(2)))
print(m)
print(m.shape)
print(m.ndim)

print("\n\n")
macierz = np.array([[1, 2], [3, 4], [5, 6]])
print(macierz)
print(macierz.shape)
print(macierz.ndim)

print("\n\n")
zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print("\n\n")
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

print("\n\n")
pusta = np.empty((2, 2))
print(pusta)
poz_1 = pusta[1, 1]
poz_2= pusta[0, 1]
print(poz_1)
print(poz_2)

print("\n\n")
macierz = np.array([[1, 2], [3, 4]])
print(macierz)
liczby = np.arange(1, 2, 0.1)
print(liczby)

print("\n\n")
liczby_lin = np.linspace(1, 2 , 5, endpoint=False)
print(liczby_lin)

print("\n\n")
z = np.indices((5, 3))
print(z)

print("\n\n")
x, y = np.mgrid[0:5, 0:5]
print(x, "\n")
print(y, "\n")


print(z[0, 0, 1])
print(z.ndim)

print("\n\n")
mat_diag_k = np.diag([a for a in range(5)])
print(mat_diag_k)

print("\n\n")
z = np.fromiter(range(5), dtype = 'int32')
print(z)
