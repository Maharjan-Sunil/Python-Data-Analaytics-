# import datetime
# print(datetime.datetime(1970, 1, 1).strftime('%Y-%d-%B'))

def find_Value(lists,value):
    
    lists.sort()
    print(lists)
    if len(lists) < 1:
        return 0
    print(f'len of lists is {len(lists)}')
    mid_point = int(len(lists)/2)
    print(f' mid point is {mid_point}')
    if(lists[mid_point] == value):
        return 1
    elif(lists[mid_point] > value):
        return find_Value(lists[:mid_point],value)
    else:
        return find_Value(lists[mid_point:],value)

list_of_num = [1,10,3,14,5,6,10]
print(find_Value(list_of_num,10))
        
    
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
