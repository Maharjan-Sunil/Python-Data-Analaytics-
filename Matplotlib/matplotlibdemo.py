import numpy as np
from matplotlib import pyplot as ply

x=np.arange(1,11)
y=x*2+5
ply.title('Rate of Success')
ply.xlabel('Hard work')
ply.ylabel('Sucesss')
ply.plot(x,y)
ply.show()

# import numpy as np 
# from matplotlib import pyplot as plt 

# x = np.arange(1,11) 
# y = 2 * x + 5 
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y) 
# plt.show()