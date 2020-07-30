#data visualization for GAS usages in Surja Residence
from matplotlib import pyplot as ply
import numpy as np

no_of_gas=[1,2,3,4,5]
no_of_days=[15,14,14,16,12]

#np_data= np_array(data)
ply.plot(no_of_gas,no_of_days)
ply.xlabel("No of Gas")
ply.ylabel("No of Days")
ply.title("Usages of Gas")
ply.show()
