import numpy as np
def voted_perceptron():
    # INITIALIZATION
    n=1
    w[1]=0
    b[1]=0
    c[1]=0

    # LOGIC
    for iter in range(1,Num_Epochs):
        for i in range(1,m):
            if y_i(w[n]+b[n])<=0:
                n=n+1
                w[n]=w[n-1]+y[i]*x[i]
                b[n]=b[n-1]+y[i]
                c[n]=1
            else:
                c[n]=c[n]+1
