def params(*param, **key_param):
    for data in param:
        print(data)
    for value in key_param.values():
        print(f'value in dict is : {value}')        

params(1,2,3,data = "manish")  

#zip
# list_name = ['manish','shyam','rita']
# mark_list={50,12,10}

# merge_list = set(zip(list_name,mark_list))
# print(merge_list)
