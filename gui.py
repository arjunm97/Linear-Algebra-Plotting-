from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



"""Front end buttons text entry and converting fucntion"""



window=Tk()

x11=StringVar()
y11=StringVar()
z11=StringVar()
#equation 2 normal
x22=StringVar()
y22=StringVar()
z22=StringVar()
#equation 3 normal
x33=StringVar()
y33=StringVar()
z33=StringVar()

u1=StringVar()
v1=StringVar()
w97=StringVar()

def Converting():
	
	#equation 1 normal
	x1=int(x11.get())
	y1=int(y11.get())
	z1=int(z11.get())
				
	#equation 2 normal
	x2=int(x22.get())
	y2=int(y22.get())
	z2=int(z22.get())
			
	#equation 3 normal
	x3=int(z33.get())
	y3=int(y33.get())
	z3=int(z33.get())
			
	#constants
	u=int(u1.get())
	v=int(v1.get())
	w=int(w97.get())
	print(x1,y1,z1,x2,y2,z2,x3,y3,z3)
	print(u,v,w)
	plotting(x1,y1,z1,x2,y2,z2,x3,y3,z3,u,v,w)

def plotting(x1,y1,z1,x2,y2,z2,x3,y3,z3,u,v,w):
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


#x1
a1=Entry(window,textvariable=x11)
a1.grid(row=0,column=1)
w1=Label(window, text="X1")
w1.grid(row=0,column=0)


#y
a2=Entry(window,textvariable=y11)
a2.grid(row=1,column=1)
w2=Label(window, text="Y1")
w2.grid(row=1,column=0)


#z1
a3=Entry(window,textvariable=z11)
a3.grid(row=2,column=1)
w3=Label(window, text="Z1")
w3.grid(row=2,column=0)

#x2
b1=Entry(window,textvariable=x22)
b1.grid(row=3,column=1)
w4=Label(window, text="X2")
w4.grid(row=3,column=0)

#y2
b2=Entry(window,textvariable=y22)
b2.grid(row=4,column=1)
w5=Label(window, text="Y2")
w5.grid(row=4,column=0)


#z2
b3=Entry(window,textvariable=z22)
b3.grid(row=5,column=1)
w6=Label(window, text="Z2")
w6.grid(row=5,column=0)


#x3
c1=Entry(window,textvariable=x33)
c1.grid(row=6,column=1)
w7=Label(window, text="X3")
w7.grid(row=6,column=0)


#y3
c2=Entry(window,textvariable=y33)
c2.grid(row=7,column=1)
w8=Label(window, text="Y3")
w8.grid(row=7,column=0)


#z3
c3=Entry(window,textvariable=z33)
c3.grid(row=8,column=1)
w9=Label(window, text="z3")
w9.grid(row=8,column=0)

#a
a=Entry(window,textvariable=u1)
a.grid(row=9,column=1)
w10=Label(window, text="Enter 1st constant")
w10.grid(row=9,column=0)

#b
b=Entry(window,textvariable=v1)
b.grid(row=10,column=1)
w11=Label(window, text="Enter 2nd constant")
w11.grid(row=10,column=0)

#c
c=Entry(window,textvariable=w97)
c.grid(row=11,column=1)
w12=Label(window, text="Enter 3rd constant")
w12.grid(row=11,column=0)


generate=Button(window,text="Generate",command=Converting)

generate.grid(row=12,column=1)


window.mainloop()


