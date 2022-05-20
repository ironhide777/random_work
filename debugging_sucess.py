from vpython import *
import numpy as np
import math
#standard property definition 
def deg2rad(theta):
    return theta*(pi/180) #rad
def rad2deg(theta):
    return theta*(180/pi) #deg
#---------------------------------------------
#Constants
rho=1000 #density kg/m^3
g=9.8 #gravity m/s^2
pi = 3.14
#body property
m=4500*.001 #mass kg material steel 8g/cm3

a=400 *.001 #length m

a_e = 50*.001

r=50 *.001 #radius m

I_x=10

I_y=10

I_z=10


#input variable
F_1=np.array([[100],[0],[0]]) #thruster force 1 N

F_2=np.array([[0],[0],[0]])#thruster force 2 N

theta_z = deg2rad(0)  #thruster rotation in z axis deg
print(theta_z)
theta_x = deg2rad(0)  #thruster rotation in x axis deg


# initial condition
h=0 #depth m

h_e = 1

t=1

t_e=10

#Equation definitoon

def f(t,theta_z,F_1,F_2,m):
    return math.sqrt(((t**2)*(F_1[0]-F_2[0])*math.cos(theta_z))/m)

def G(t,theta_x,theta_z,F_1,F_2,m):
    return math.sqrt(((t**2)*(F_1[1]-F_2[1])*math.cos(theta_x)*math.sin(theta_z))/m)

def H(t,theta_x,theta_z,F_1,F_2,m,a,g,r,h,rho,pi):
    psinx= (math.sin(theta_x))
    psinz= (math.sin(theta_z))
    print(psinx)
    print(psinz)
    force1=(F_1[2]*psinx*psinz)
    force2=(F_2[2]*psinx*psinz)
    force3=(a*g*h*r*rho)
    force4=(pi*g*(r**2)*rho*(a+((4*r)/3)))
    force5=(g*m)
    T=(t**2)
    print('force1=',force1)
    print('force2=',force2)
    print('force3=',force3)
    print('force4=',force4)
    print('force5=',force5)
    print('T=',T)
    return math.sqrt((T*(force5+force1-force2+force3-force4))/m)

def phi(t,theta_z,F_1,a,a_e,I_x):
    phicos=math.cos(theta_z)
    return math.sqrt(((t**2)*F_1[0]*(phicos)*(a+a_e))/I_x)
def theta(t,theta_x,theta_z,F_1,I_y,a,a_e):
    return math.sqrt(((t**2)*F_1[1]*math.cos(theta_x)*math.sin(theta_z)*(a+a_e))/I_y)
def psi(t,theta_x,theta_z,F_1,I_z,a,a_e):
    return math.sqrt(((t**2)*F_1[2]*math.sin(theta_x)*math.sin(theta_z)*(a+a_e))/I_z)
print(phi(t,theta_z,F_1,a,a_e,I_x))

#Execution intruction
#visual display code - vpython

#program settings
scene = canvas(title='Force demonstartion', width=1000, height=1000, center=vector(0,0,0), background=vector(.8,.8,.8))

print(scene.width/2)

canvas_center = points(pos=vector(0,0,0), radius=5, color=color.yellow, opacity = .5)

pointer_XC = arrow(pos=vector(0,0,0),axis=vector(60,0,0),shaftwidth=5,color = color.red)

pointer_YC = arrow(pos=vector(0,0,0),axis=vector(0,60,0),shaftwidth=5,color = color.green)

pointer_ZC = arrow(pos=vector(0,0,0),axis=vector(0,0,60),shaftwidth=5,color = color.black)



#coordinate settings
World_coordinate = points(pos=vector(-1000,-1000,1000), radius=5, color=color.yellow)

pointer_X = arrow(pos=vector(-1000,-1000,1000),axis=vector(100,0,0),shaftwidth=5,color = color.red)

pointer_Y = arrow(pos=vector(-1000,-1000,1000),axis=vector(0,100,0),shaftwidth=5,color = color.green)

pointer_Z = arrow(pos=vector(-1000,-1000,1000),axis=vector(0,0,100),shaftwidth=5,color = color.black)

#environment settings 
limitX=2000
plane_1=box(pos=vector(0,0,0), size=vector(limitX,1,2000),color=color.blue, opacity = .1)
plane_2=box(pos=vector(0,0,0), size=vector(1,2000,2000),color=color.blue, opacity = .1)
X_axis_line = box(pos=vector(0,0,0), size=vector(2000,5,5), color=color.black, opacity = .5)
Y_axis_line = box(pos=vector(0,0,0), size=vector(5,2000,0), color=color.black, opacity = .5)
Z_axis_line = box(pos=vector(0,0,0), size=vector(5,5,2000), color=color.black, opacity = .5)
#object setting

#variables
xaxis_offset = 60


ship_b1 = cylinder(pos = vector(xaxis_offset+25,0,0), axis=vector(100,0,0),radius=25, color=color.red, opacity = 1)

ship_b2 = sphere(pos = vector(xaxis_offset+25,0,0), radius = 25, color=color.red, opacity = 1 )

ship_b3 = sphere(pos = vector(xaxis_offset+125,0,0), radius = 25, color=color.red, opacity = 1)

ship = compound( [ship_b1, ship_b2, ship_b3 ], pos=vector(135,0,0) )

#ship body coordinate 

body_coordinate = points(pos=ship_b1.pos-vector(25,0,0), radius=5, color=color.yellow)

pointer_X = arrow(pos=ship_b1.pos-vector(25,0,0),axis=vector(60,0,0),shaftwidth=5,color = color.red)

pointer_Y = arrow(pos=ship_b1.pos-vector(25,0,0),axis=vector(0,0,60),shaftwidth=5,color = color.green)

pointer_Z = arrow(pos=ship_b1.pos-vector(25,0,0),axis=vector(0,-60,0),shaftwidth=5,color = color.black)


#now ypython default coordinate or vector(0,0,0) will be at the center of the body

#simulation
D_X = []

while t <= t_e:
    
    rate(10)
    D_X_F = [[f(t,theta_z,F_1,F_2,m)],
             [G(t,theta_x,theta_z,F_1,F_2,m)],
             [H(t,theta_x,theta_z,F_1,F_2,m,a,g,r,h,rho,pi)]]
   
    #f(t,theta_z,F_1,F_2,m) ship x axis
    #G(t,theta_x,theta_z,F_1,F_2,m) ship y axis
    #H(t,theta_x,theta_z,F_1,F_2,m,a,l,g,r,h,rho,pi) ship z axis
    
    #X_axis_value = f(t,theta_z,F_1,F_2,m)
    Depth_Y_axis_value = H(t,theta_x,theta_z,F_1,F_2,m,a,g,r,h,rho,pi)
    #Y_axis_value = G(t,theta_x,theta_z,F_1,F_2,m)
    
    #if X_axis_value  <0 :
     #   ship.pos=vector(135+X_axis_value,Depth_Y_axis_value,Y_axis_value)
    #elif  X_axis_value >0:
     #   ship.pos=vector(135+X_axis_value,Depth_Y_axis_value,Y_axis_value)
    #else :
    #    ship.pos=vector(135,Depth_Y_axis_value,Y_axis_value)

       

    D_X.append( D_X_F)
    h_e = h_e+1
    h=Depth_Y_axis_value
    t+=1
    
    print("f(t,theta_z,F_1,F_2,m)=", f(t,theta_z,F_1,F_2,m))
    print("G(t,theta_x,theta_z,F_1,F_2,m)=", G(t,theta_x,theta_z,F_1,F_2,m))
    print("H(t,theta_x,theta_z,F_1,F_2,m,a,g,r,h,rho,pi)=",H(t,theta_x,theta_z,F_1,F_2,m,a,g,r,h,rho,pi))
    
    
    print(t)
    t+=1
    
print(D_X)   

    


print("end of program")
