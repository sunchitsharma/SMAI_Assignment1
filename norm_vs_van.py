import normal_perceptron as nop
import voted_perceptron as vop
import matplotlib.pyplot as plt

accr_nop=nop.main_part()
accr_nop1=accr_nop[0:13]
accr_nop2=accr_nop[13:]
accr_vop=vop.main_part()
accr_vop1=accr_vop[0:13]
accr_vop2=accr_vop[13:]

epoch_list = [1,2,3,5,10,15,20,25,30,35,40,45,50]## EPOCH LIST
x=input("1 for Cancer dataset , 2 for Inosphere dataset : ")
if x==1:
    plt.plot(epoch_list,accr_nop1,label="Cancer : Vanila")
    plt.plot(epoch_list,accr_vop1,label="Cancer : Voted")
else:
    plt.plot(epoch_list,accr_nop2,label="Inosphere : Vanila")
    plt.plot(epoch_list,accr_vop2,label="Inosphere : Voted")
plt.legend(loc = 'center left')
plt.show()
