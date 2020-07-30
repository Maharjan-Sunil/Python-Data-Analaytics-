import numpy as np
#list_of_lists = [[1,4,1],[1,3,1],[2,2,2]] 
#data = np.array(list_of_lists)

#add row only and for column axis =0
# sum = data.sum(axis=0)
#sum = data.sum()
#print(sum)

#can direct add and do other mathematics treat as elemenet
#add_by_1 = data + 1
#print(add_by_1)

#shape
#print(data.shape)
#print(type(data))

#slicing in np array
#print(data[:,:-2])


#random 
# sale_of_coffee = np.random.randint(20,100,size=(4,7)) #generate random value from (start,end)
# print(sale_of_coffee)
# print(sale_of_coffee.argmax()) #return index that have high value 
# print(sale_of_coffee.max())

list_a = [[1,2,1],[2,22,2]]
list_b = [[2,6,2],[2,21,2]]
a = np.array(list_a)
b = np.array(list_b)
print(a)
print(b)
print(a+b)
