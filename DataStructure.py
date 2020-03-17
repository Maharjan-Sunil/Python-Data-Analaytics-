import pandas as pa

series = ['manish','hari','shyam']

seriesWithIndex = pa.Series(series,index=['a','b','c'])
print (seriesWithIndex)

dataFrame=[['Alex',10],['Bob',12]]

dataFrameWithColumns=pa.DataFrame(dataFrame,index=['i','ii'],columns=["Name","Age"])
print (dataFrameWithColumns)

dataPanel = pa.Panel()
print (dataPanel)


#panel remain