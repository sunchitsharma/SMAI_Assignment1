import numpy as np
import matplotlib.pyplot as plt
import normal_perceptron as vp

def LDA_1(m1,m2):
    mean_x1=np.mean(m1[:,0])
    mean_y1=np.mean(m1[:,1])
    mean_x2=np.mean(m2[:,0])
    mean_y2=np.mean(m2[:,1])

    mean1=[mean_x1,mean_y1]
    mean2=[mean_x2,mean_y2]
    mean1=np.array(mean1)
    mean2=np.array(mean2)

    m11=[]
    m22=[]

    for i in range(0,len(m1)):
        t1=m1[i][0]-mean1[0]
        t2=m1[i][1]-mean1[1]
        m11.append([t1,t2])

    for i in range(0,len(m2)):
        t1=m2[i][0]-mean2[0]
        t2=m2[i][1]-mean2[1]
        m22.append([t1,t2])
    m11=np.array(m11)
    m22=np.array(m22)

    m11_T=np.transpose(m11)
    m22_T=np.transpose(m22)

    m1_F=np.dot(m11_T,m11)
    m2_F=np.dot(m22_T,m22)

    m_F=m1_F+m2_F

    i_m_F=np.linalg.inv(m_F)
    mean = mean1-mean2
    w=np.dot(i_m_F,mean)
    w=w/np.linalg.norm(w)
    return w

def main_func():

    mat_1=[[3,3],[3,0],[2,1],[0,2]]
    mat_2=[[-1,1],[0,0],[-1,-1],[1,0]]
    m1=np.array(mat_1)
    m2=np.array(mat_2)
    weights=LDA_1(m1,m2)
    class1 = mat_1
    class2 = mat_2

    # STARTING PLOT
    pl1 = zip(*mat_1)[0]; d1x2 = zip(*mat_1)[1]
    pl2 = zip(*mat_2)[0]; d2x2 = zip(*mat_2)[1]

    c1 = plt.scatter(pl1, d1x2, c = "red", label = "C1")
    c2 = plt.scatter(pl2, d2x2, c = "green", label = "C2")

    points = []
    dp_1 = np.dot(mat_1, weights)
    for val in dp_1:
    	points.append(np.dot(val, weights))
    total_points = [[[i[0],i[1],1],1] for i in points]
    plt.plot(zip(*points)[0], zip(*points)[1], "rx")

    for i in range(len(points)):
    	plt.plot([class1[i][0], points[i][0]], [class1[i][1], points[i][1]], 'r--')

    dp_1 = np.dot(mat_2, weights)
    points = []
    for val in dp_1:
    	points.append(np.dot(val, weights))
    total_points += [[[i[0],i[1],1],-1] for i in points]
    plt.plot(zip(*points)[0], zip(*points)[1], "gx")

    for i in range(len(points)):
    	plt.plot([class2[i][0], points[i][0]], [class2[i][1], points[i][1]], 'g--')

    x = np.array(range(-2, 5))
    y = eval("(x - points[0][0]) * (weights[1] / weights[0]) + points[0][1]")
    discriminant = plt.plot(x, y, label = 'discriminant')

    ans = []

    for i in total_points:
        temp=[]
        temp.extend(i[0])
        temp.append(i[1])
        ans.append(temp)

    ## GETTING CLASSIFIER
    w = vp.train_weigths(ans,1, 10000)
    del w[0]

    # PLOTTING CLASSIFIER
    x = np.array(range(-2, 5))
    y = eval("x * (-w[0] / w[1]) - (w[2] / w[1])")
    classifier = plt.plot(x, y, label = 'classifier')


#main_func()
