import numpy as np
import matplotlib.pyplot as plt
def least_square(A):
    A_T=np.transpose(A)
    X=np.matmul(A_T,A)
    Y=np.linalg.inv(X)
    Z=np.matmul(Y,A_T)
    b=[1,1,1,1,1,1,1,1]
    b=np.array(b)
    b_T=b.reshape(len(b),1)
    w=np.matmul(Z,b_T)
    return w

def main_func():
    mat_1=[[3,3,1],[3,0,1],[2,1,1],[0,1.5,1]]
    u_mat_2=[[-1,1,1],[0,0,1],[-1,-1,1],[1,0,1]]
    mat_2=[[1,-1,-1],[0,0,-1],[1,1,-1],[-1,0,-1]]

    over_mat= mat_1+mat_2
    A = np.array(over_mat)
    w= least_square(A)
    x1=[]
    y1=[]
    x2=[]
    y2=[]

    for i in mat_1:
        x1.append(i[0])
        y1.append(i[1])


    for i in u_mat_2:
        x2.append(i[0])
        y2.append(i[1])

    plot1= plt.scatter(x1,y1,c="red",label="FIRST")
    plot2= plt.scatter(x2,y2,c="green",label="SECOND")
    w=np.transpose(w)
    x=np.array(range(-2,4))
    y=eval("x*(-w[0][0]/w[0][1])-(w[0][2]/w[0][1])")
    classifier=plt.plot(x,y,label="LMS classifier")

## RUN CODE #########
#main_func()
#####################
