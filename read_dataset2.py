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
        answer.append(temp)

    random.shuffle(answer)
    random.shuffle(answer)
    random.shuffle(answer)
    #print answer
    for i in range(0,len(answer)):
        if (str)(answer[i][-1])=='g\n':
            label.append(0)
            answer[i][-1]=0.0
        else:
            label.append(1)
            answer[i][-1]=1.0



    answer=filter(answer)

    #print answer
    #print label
    return answer,label


def filter(x):
    answer = []
    del x[-1]
    for i in x:
        answer.append(i)

        for i in range(0,len(answer)):
            for j in range(0,len(answer[i])):
                answer[i][j]=(float)(answer[i][j])
    return answer

## TEST CODE
fileread('inosphere_dataset')
