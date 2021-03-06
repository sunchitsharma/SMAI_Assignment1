import random as rn
import numpy as np
import read_dataset as rd
import read_dataset2 as rd2
weights=[]
dataset=None
label=None
## MAIN CONTROLLER
accr=[]
def main_part():

    l_rate = input("Enter The Learning Rate : ")
    for alpha in range(0,2):
        if alpha ==0:
            print "##########breast_cancer_dataset##############"
            dataset,label= rd.fileread('breast_cancer_dataset')
        else:
            print "#############inposhere_dataset###############"
            dataset,label=rd2.fileread('inosphere_dataset')

        epoch_list = [1,2,3,5,10,15,20,25,30,35,40,45,50]## EPOCH LIST
        for c_epoch in epoch_list:
            weights=[]
            n=len(dataset)/10
            n_epoch = c_epoch
            r_dict = ten_parts(dataset)
            acc=[]
            for i in range(0,10):
                del weights[:]
                trainmat=[]
                testmat=None
                for j in range(0,10):
                    if(j==i):
                        testmat=r_dict[i]
                    else:
                        trainmat.extend(r_dict[i])
                weights = train_weigths(trainmat,l_rate,n_epoch)
                #print weights
                pred=[]
                for row in testmat:
                    prediction = predict(row,weights)
                    pred.append(prediction)
                currpos=i*n
                act=[]
                for j in range(currpos,currpos+n):
                    if(j==len(label)):
                        break
                    else:
                        act.append(label[j])
                accuracy = calculate_accuracy(act,pred)
                acc.append(accuracy)
            print "At Epoch : "+(str)(c_epoch)+" Accuracy : "+(str)((float)(sum(acc))/(float)(len(acc)))
            accr.append((float)(sum(acc))/(float)(len(acc)))
        print "#############################################"
    return accr

        #print(weights)


## DEVIDE IN 10 PARTS

def ten_parts(dataset):
    r_dict = {}
    currele = 0
    n= len(dataset)/10
    for i in range(0,10):
        temp=[]
        for j in range(0,n):
            if(dataset[-1]==dataset[currele]):
                temp.append(dataset[currele])
                currele+=1
                break
            else:
                temp.append(dataset[currele])
                currele+=1
        r_dict[i]=temp
    return r_dict


## CALCULATE ACCURACY

def calculate_accuracy(actual,predicted):
    count=0
    for i in range(0,len(actual)):
        if(actual[i]==predicted[i]):
            count=count+1
    accuracy = ((float)(count)/(float)(len(actual)))*100.00
    return accuracy

## PREDICTION ALGORITHM

def predict(row,weights):
    s=0
    for c_wt in weights:
        activation = c_wt[0][0]
        for i in range(len(row)-1):
            activation+=c_wt[0][i+1]*row[i]
        if activation >= 0.0 :
            sign = 1
        else :
            sign = -1
        s+=c_wt[1]*sign
    if s>=0:
        return 1.0
    else:
        return 0.0


## PREDICTION FOR TRAINING


def predict2(row,weights):

    activation = weights[0]
    for i in range(len(row)-1):
        activation+=weights[i+1]*row[i]
    if activation >= 0.0 :
        return 1.0
    else:
        return 0.0



## TRAINING THE PERCEPTRON
ret_list=[]
def train_weigths(train, l_rate, n_epoch):
    c=0
    for i in range(0,len(train[0])+1):
        weights.append(0.0)
    for epoch in range(n_epoch):
        for row in train:
            prediction = predict2(row,weights)
            error = row[-1]-prediction
            if error == 0 :
                c=c+1
            else:
                t_tup=(weights,c)
                ret_list.append(t_tup)
                c=0
                weights[0]=weights[0]+l_rate*error
                for i in range(len(row)):
                    weights[i+1]=weights[i+1]+l_rate*error*row[i]
    t_tup=(weights,c)
    ret_list.append(t_tup)
    return ret_list

## NORMAL PERCEPTRON

def preceptron(train,test,lrate,n_epoch):
    predictions=[]
    weights = train_weigths(train,l_rate,n_epoch)
    for row in test:
        prediction = predict(row,weights)
        predictions.append(prediction)
    return predictions




#################### RUNNER #####################
#main_part()
#################################################

# TEST CODES #####################################

# dataset = [[2.7810836,2.550537003,0],
# 	[1.465489372,2.362125076,0],
# 	[3.396561688,4.400293529,0],
# 	[1.38807019,1.850220317,0],
# 	[3.06407232,3.005305973,0],
# 	[7.627531214,2.759262235,1],
# 	[5.332441248,2.088626775,1],
# 	[6.922596716,1.77106367,1],
# 	[8.675418651,-0.242068655,1],
# 	[7.673756466,3.508563011,1]]
#
# #weights = [-0.1, 0.20653640140000007, -0.23418117710000003]
#
# # TEST TRAINING ALGORITHM #########################
#
# l_rate = 0.1
# n_epoch = 5
# v_weights = train_weigths(dataset,l_rate,n_epoch)
# print(v_weights)
