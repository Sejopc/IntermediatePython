# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

#same as above
def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,7))

####
points20 = [(1,2), (15,1), (5,-1), (10,4)]
points20_sorted = sorted(points20) #by default, sorts by X index
print(points20)
print(points20_sorted)
print(sorted(points20, key=lambda x: x[1])) #sorts by Y index

###
def sort_by_y(x):
    return x[1]

print(sorted(points20_sorted, key=sort_by_y))

###
print(sorted(points20, key=lambda x: x[0] + x[1])) # sorts by the sum of x and y


### MAP Function ###
# map(func,seq)

a = [1,2,3,4,5,6]
b = map(lambda x: x*2, a)
print(list(b))

# same as above using list comprehension
c = [x * 2 for x in a]
print(c)

### FILTER Function ###
# filter(func,seq)
c = filter(lambda x:x%2==0, a)
print(list(c))

# same as above using list comprehension
c = [x for x in a if x %2 == 0]
print(c)

## REDUCE function ##
# reduce(func,seq)
from functools import reduce
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
