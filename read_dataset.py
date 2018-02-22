import re
import random
def fileread(name_of_file):
    f=None
    try:
        f= open(name_of_file,"r")
    except:
        print " Sorry Enter a valid file name "
        exit(0)

    dicdata=[]
    strdata = f.readlines()
    label=[]
    answer=[]
    temp=[]
    for i in strdata:
        temp=i.split(",")
        del temp[0]
        answer.append(temp)

    answer=filter(answer)

    
    #print answer
    for i in range(0,len(answer)):
        label.append(answer[i][-1]/2-1)
        answer[i][-1]=answer[i][-1]/2-1
    return answer,label

def filter(x):
    answer = []
    del x[-1]
    for i in x:
        i[-1]=i[-1][0:len(i[-1])-1]
        if '?' not in i:
            answer.append(i)

        for i in range(0,len(answer)):
            for j in range(0,len(answer[i])):
                answer[i][j]=(float)(answer[i][j])
    return answer

## TEST CODE
fileread('breast_cancer_dataset')
