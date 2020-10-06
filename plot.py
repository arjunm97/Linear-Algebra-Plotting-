import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



x1=1
y1=-2
z1=1
#equation 2 normal
x2=0
y2=2
z2=-8
#equation 3 normal
x3=-4
y3=5
z3=9

u=0
v=8
w=-9


mat=[[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]
a=np.array(mat)
b=np.array([u,v,w])
x = np.linalg.solve(a, b)
print(x)
#x=np.array(x)


point  = x
normal1 =np.array([x1,y1,z1])
normal2 =np.array([x2,y2,z2])
normal3 =np.array([x3,y3,z3])

#print(normal1)

d1 = -point.dot(normal1)
d2 = -point.dot(normal2)
d3 = -point.dot(normal3)

# create x,y
xx1, yy1 = np.meshgrid(range(10), range(10))
xx2, yy2 = np.meshgrid(range(10), range(10))
xx3, yy3 = np.meshgrid(range(10), range(10))

# calculate corresponding z
z1 = (-normal1[0] * xx1 - normal1[1] * yy1 - d1) * 1. /normal1[2]
z2 = (-normal2[0] * xx2 - normal2[1] * yy2 - d2) * 1. /normal2[2]
z3 = (-normal3[0] * xx3 - normal3[1] * yy3 - d3) * 1. /normal3[2]

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx1, yy1, z1,alpha=0.75)
plt3d.plot_surface(xx2, yy2, z2,alpha=0.75)
plt3d.plot_surface(xx3, yy3, z3,alpha=0.75)
plt.show()


