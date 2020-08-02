import numpy as np
an_array = [[2,4,6,],[1,3,5]]
np_array = np.array(an_array)

print(np_array)
# print(np_array.shape)
# np_array.reshape(3,2).shape
# print(np_array.shape)


# a = [1,2]
# b=[3,4]

#print(np.dot(a, b)) # inner product of two arrays
#print(np.outer(a, b)) # outer product of two arrays #multiply each element

# transpose
# print(np_array.transpose())

#change or mutate the value of specific poistion aij(row and column) start with 0 index
np_array[1,1]=7
print(np_array)

#a_array = [2,4,6]
#b_array = [1,3,5]

#concatenation
#print(np.hstack((a_array,b_array))) #horizontal
#print(np.vstack((a_array,b_array))) #vertical
#print(np.dstack((a_array,b_array))) #dimension (transpose)


#ravel transform in one dimensional
# print(np_array.ravel().shape)

#arrange return list 
print(np.arange(1,100,5))