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
        
    
