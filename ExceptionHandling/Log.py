import logging
logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode= 'w')

#by default hierarchy for logging
# DEBUG
# INFO
# Warning
# error
# critical

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        logging.error(f'cannot be divided by zero')
        return None

print(division(1,0))

#isInstance

tuples = (1,2,3)
if(isinstance(tuples,dict)):
    print ('true')
