# Retoji matrica "koordinaciu" pavidale

from scipy import sparse
import numpy as np
from matplotlib import pyplot

# is staciakampes i retaja:
A=np.matrix([[ 2, -1,  0,  0,  0,  0, -1],
             [-1,  2, -1,  0,  0,  0,  0],
             [ 0, -1,  2, -1,  0,  0,  0],
             [ 0,  0, -1,  2, -1,  0,  0],
             [ 0,  0,  0, -1,  2, -1,  0],
             [ 0,  0,  0,  0, -1,  2, -1],
             [-1,  0,  0,  0,  0, -1,  2]]).astype(np.float)
print(A)

As = sparse.csr_matrix(A)
print(As)

# is retosios i staciakampe:
B=As.toarray()
print(B)

# retosios formavimas pagal duotas elementu "koordinates"
i=np.array([1,  2,  7,  1,  2,  3,  2,  3,  4,  3,  4,  5,   4,  5,  6,  5,  6,  7,  1,  6,  7])-1;
j=np.array([1,  1,  1,  2,  2,  2,  3,  3,  3,  4,  4,  4,   5,  5,  5,  6,  6,  6,  7,  7,  7])-1;
s=np.array([2, -1, -1, -1,  2, -1, -1,  2, -1, -1,  2, -1,  -1,  2, -1, -1,  2, -1, -1, -1,  2 ]);

Asparse=sparse.coo_matrix((s, (i, j)))
print(Asparse)


As[0,4]=390
r,c=As.nonzero()
print(r)
print(c)
print(As[r,c])


pyplot.spy(Asparse);
pyplot.show();
