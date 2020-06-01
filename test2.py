# import datetime
# print(datetime.datetime(1970, 1, 1).strftime('%Y-%d-%B'))

from matplotlib import pyplot as py

sitename=["allfootball","nepalfreelance","school","ismartmandu",'mysql','swscfa']
memory=[3.15,1.63,0.77,0.70,0.54,0.41]
#labels=['science','Math','Account']
py.plot(sitename,memory)
py.xlabel("Website Name")
py.ylabel("Memory allocated in GB")
py.title("Usage of Total Memory (9GB) for different site")
py.text('allfootballplay',3.15,'high allocated memory')
py.grid(True)
# py.xticks[[80,75,60,55,75,65,55,80],['Science','Math','Nepali','English','Computer','Opt','Health','Account']]
py.show()