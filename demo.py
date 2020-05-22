import numpy as np

from matplotlib import pyplot as ply
#to be more specific 

data=[1,2,3,4]
#print('the last element in data is ' + str(data[-1]))

#2D array
datas=[1,2,3,4,5]
weight = [[1,2,3],[10,14,9]]
height = [[1,2,3], [5,6,4]]

np_height = np.array(height)
np_weight=np.array(weight)

#slicing in python
#print('the last 2 element in data is ' +str(datas[-1:0]))

#shape attribute
# print(np_height.shape)
# print(np_weight[0,:1])


#matplotlib

x=[1,2,3,4]
y=[10,15,13,9]
# ply.title("Score in Math")
# ply.xlabel("Student")
# ply.ylabel("Score")
# ply.plot(x,y)
# ply.show()

#math mathematical tools
print('the average score is ' + str(np.mean(y)))
print('the standard deviation in score is ' + str(round(np.std(y),2)))