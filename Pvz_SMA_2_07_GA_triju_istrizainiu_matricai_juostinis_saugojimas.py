
import numpy as np
from PyFunkcijos import *

# textbox isvedimui
T=ScrollTextBox(100,20) # sukurti teksto isvedimo langa
T.insert(END,"# ********************* Gauso algoritmas  ****************************")


# -------------------iseities duomnenys:
# koeficientu matricos staciakampis pavidalas:
A=np.matrix([[ 1, -1,  0,  0,  0,  0,  0],
             [-1,  2, -1,  0,  0,  0,  0],
             [ 0, -1,  2, -1,  0,  0,  0],
             [ 0,  0, -1,  2, -1,  0,  0],
             [ 0,  0,  0, -1,  2, -1,  0],
             [ 0,  0,  0,  0, -1,  2, -1],
             [ 0,  0,  0,  0,  0, -1,  2]]).astype(np.float)

b=np.matrix([[2],[0],[0],[0],[0],[0],[0]])
n=(np.shape(A))[0]   # lygciu skaicius nustatomas pagal ivesta matrica A

# koeficientu matricos juostinis pavidalas
Ar=np.zeros(shape=(n,3));
for i in range (0,n):
    if i == 0     : Ar[0,1:3]=A[i,0:2]
    elif i == n-1 : Ar[n-1,0:2]=A[n-1,n-2:n]
    else          : Ar[i,0:3]=A[i,i-1:i+2]
SpausdintiMatrica(Ar,T,'Ar');

A1=np.hstack((Ar,b))  # matrica ir laisvuju nariu vektorius sublokuojami

SpausdintiMatrica(A,T,'A');SpausdintiMatrica(Ar,T,'Ar');SpausdintiMatrica(b,T,'b');SpausdintiMatrica(A1,T,'A1');SpausdintiMatrica(n,T,'n');
#print(A);print(b);print(n);print(nb);print(AA)

# tiesioginis etapas: 

# Gauso algoritmo tiesioginis etapas:
for i in range (0,n-1):
       A1[i+1,[1,3]]=A1[i+1,[1,3]]-A1[i,[2,3]]*A1[i+1,0]/A1[i,1]
       A1[i+1,0]=0
       SpausdintiMatrica(A1,T,'A1');

# Gauso algoritmo atgalinis etapas:
x=np.zeros(shape=(n,1))
x[n-1]=A1[n-1,3]/A1[n-1,1];
SpausdintiMatrica(x,T,'x');
for i in range (n-2,-1,-1) :
    x[i]=(A1[i,3]-A1[i,2]*x[i+1])/A1[i,1]
    SpausdintiMatrica(x,T,'x');


T.insert(END,"sprendinys:");SpausdintiMatrica(x,T,'x');
T.insert(END,"------------ sprendinio patikrinimas ----------------");
liekana=A.dot(x)-b;SpausdintiMatrica(liekana,T,'liekana');
SpausdintiMatrica(np.linalg.norm(liekana)/ np.linalg.norm(x),T,"bendra santykine paklaida:")


str1=input("Baigti darba? Press Enter \n")


