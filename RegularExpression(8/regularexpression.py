import re

def return_number(text):
    search_data_number = re.search(r"(\d+)",text)
    print(search_data_number.group(1))
    print(search_data_number.groups()) #return tupls
    findall_data_number = re.findall(r"(\d+)",text)
    print(findall_data_number) #return list

info = 'I was in position of 10 but ram was in 1'
return_number(info)


