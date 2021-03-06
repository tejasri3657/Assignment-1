# -*- coding: utf-8 -*-
"""Assignment-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qdPbt10mlaXsUCYs-IMK9Pz9IEDnhxtm
"""

# -*- coding: utf-8 -*-
"""Assignment-1.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1AJAG_SE0PGcIzNhuqjYi-4mTpahYdD_0
"""

# -*- coding: utf-8 -*-

"""Assignment-1.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1Dmw-_XJsPZSs3_eh7p92ARj4re39WuU5
"""


import numpy as np


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
#def line_gen(A,B):
#  len =10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB

#Generate line intercepts
def line_icepts(n,c):
  e1 = np.array([1,0]) 
  e2 = np.array([0,1]) 
  A = c*e1/(n@e1)
  B = c*e2/(n@e2)
  return A,B

#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
#Generate line points

def line_norm_eq(n,c,k):
  len =10
  dim = n.shape[0]
  m = omat@n
  m = m/np.linalg.norm(m)
#  x_AB = np.zeros((dim,2*len))
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k[0],k[1],len)
#  print(lam_1)
#  lam_2 = np.linspace(0,k2,len)
  if c==0:
    for i in range(len):
      temp1 = lam_1[i]*m
      x_AB[:,i]= temp1.T
  else:
    A,B = line_icepts(n,c)
    for i in range(len):
      temp1 = A + lam_1[i]*m
      x_AB[:,i]= temp1.T
#    temp2 = B + lam_2[i]*m
#    x_AB[:,i+len]= temp2.T
  return x_AB

#def line_dir_pt(m,A, dim):
#  len = 10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,10,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*m
#    x_AB[:,i]= temp1.T
#  return x_AB


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P

#Code by A.Tejasri
#June 1,2021
#Drawing a isosceles triangle  
#Q.No.2.16



import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *


#Sides
b = 6.5
c = 6.5
a = 10.6


#Coordinates of B (p, q)
p = (b**2 + c**2-a**2 )/(2*b)
q = np.sqrt(c**2-p**2)
print("Coordinates of B are ", p,q)


#Triangle vertices 
B = np.array([p, q])
A = np.array([0,0]) 
C = np.array([b,0])


#Generating all lines
x_AC = line_gen(A,C)
x_BA = line_gen(B,A)
x_CB = line_gen(C,B)


#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BA[0,:],x_BA[1,:],label='$BA$')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')


plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.2), A[1] * (1) , 'A')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')



#if using termux
#plt.savefig('./tri_sss.pdf')
#plt.savefig('./tri_sss.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_sss.pdf"))
#else
plt.show()