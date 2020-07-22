def return_Mercy_Number(p):
    return 2 ** p - 1

# print(return_Mercy_Number(5))

def is_Prime(number):
    if number <=1:
        return False
    for num in range(2,number):
        if number % num ==0:
            return False
    return True

def get_Prime_Number(s,e):
    return [return_Mercy_Number(num) for num in range(s,e+1) if is_Prime(num)]

print(get_Prime_Number(1,7))