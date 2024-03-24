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
mat_diag_k = np.diag([a for a in range(7)], k=1)
print(mat_diag_k)

print("\n\n")
z = np.fromiter(range(5), dtype = 'int32')
print(z)

print("\n\n")
znaki = b'abcdef'
zn1 = np.frombuffer(znaki, dtype = 'S1')
print(zn1)
print("\n\n")
zn2 = np.frombuffer(znaki, dtype='S2')
print(zn2, "\n")

znaki = 'abcdef'
zn3 = np.array(list(znaki))
zn4 = np.array(list(znaki), dtype='S1')
zn5 = np.array(list(b'abcdef'))
zn6 = np.fromiter(znaki, dtype='S1')
zn7 = np.fromiter(znaki, dtype='U1')
print(zn3, "\n")
print(zn4, "\n")
print(zn5, "\n")
print(zn6, "\n")
print(zn7, "\n")

mat = np.ones((2, 2))
mat_1 = np.ones((2, 2))
mat = mat + mat_1
print(mat, "\n")
print(mat - mat_1, "\n")
print(mat*mat_1, "\n")
print(mat/mat_1, "\n")


a = np.dot(mat, mat_1)
print(a, "\n")
b = mat.dot(mat_1)
print(b, "\n")

a = np.arange(10)
print(a, "\n")
s = slice(2,7,2)
print(a[s], "\n")
s = range(2,7,2)
print(a[s], "\n")
print(a[2:7:2], "\n")
print(a[1:], "\n")
print(a[2:5], "\n")

mat = np.arange(25)

mat = mat.reshape((5, 5))
print(mat[1:], "\n")
print(mat[:1], "\n")
print(mat[:, -1:], "\n")
print(mat[2:6, 1:k3], "\n")
print(mat[:, range(2,6,2)], "\n")

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x, "\n")
rows = np.array([[0,0], [3,3]])
cols = np.array([[0,2],[0,2]])
y=x[rows, cols]
print(y)