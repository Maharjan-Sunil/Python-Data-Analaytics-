#@decorator to change the behaviour of method and class
def decorator_method(func):
    def wrapper(a,b):
        result = func(a,b)
        if result < 0:
            return None
        else: 
            return result
    return wrapper

def sub(a,b):
    return a -b

obj = decorator_method(sub)
print(obj(5,2))
