# Errors and Exceptions
# a = 5 print(a) # syntax Error
# print(a)) #syntax Error

# a = 5 + '10' # TypeError
# import somemodulethatdoesnotexist # ModuleNotFound Error
# a = 5
# b = c #NameError
# f = open('somefile.txt') # FileNotFoundError
a = [1,2,3]
a.remove(1)
print(a)
#a.remove(4) # ValueError

# a[4] # IndexError
my_dict = {'name':'Max'}
# my_dict['age'] # KeyError

### Raise an exception to occur when a certain condition is met ###
x = -5
#if x < 0:
#    raise Exception('x should be positive')

#x = 5
#if x < 0:
#    raise Exception('x should be positive')

### Assert statement ###
y = -5
#assert(y>=0), 'y is not positive'

### Try, except block ###
try:
    a = 5 / 0
except(ZeroDivisionError): #or simply put except
    print("Cannot divide by 0")

try:
    b = 5 / 0
except Exception as e:
    print(e)

try:
    c = 5 / 1
    b = c + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: # ran if no exception occur
    print('Everything is fine')

try:
    c = 5 / 1
    b = c + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: # ran if no exception occur
    print('Everything is fine')

try:
    c = 5 / 1
    b = c + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: # ran if no exception occur
    print('Everything is fine again')
finally: # run always, regardless if there's an exception or not
    print('Cleaning up...')

### Defining our own Exceptions ###
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

#test_value(200)

try:
    test_value(300)
except ValueTooHighError as e:
    print(e)


class ValueTooSmall(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value2(x):
    if x < 5:
        raise ValueTooSmall('Value is too small', x)

try:
    test_value2(3)
except ValueTooHighError as e:
    print(e)
except ValueTooSmall as e:
    print(e.message, e.value)
