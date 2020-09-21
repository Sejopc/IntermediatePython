# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
print("###### Product ######")
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)
print(list(prod))

c = [5]
prod2 = product(a,c, repeat=2)
print(list(prod2))

print("###### Permutations ######")
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
perm2 = permutations(a, 2) #lenght of 2
print(list(perm2))

print("###### Combinations ######")
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a, 2)
print(list(comb))

from itertools import combinations, combinations_with_replacement
b = [1,2,3,4]
comb = combinations_with_replacement(b, 2)
print(list(comb))

print("###### Accumulate ######")
from itertools import accumulate # it will compute the sums (or multiplications)
import operator
c = [1,2,3,4]
acc = accumulate(c)
print(c)
print(list(acc))
acc2 = accumulate(c, func=operator.mul)
print(c)
print(list(acc2))
c2 = [1,2,5,4,3]
acc3 = accumulate(c2, func=max)
print(c2)
print(list(acc3))

print("###### Groupby ######")
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key,value in group_obj:
    print(key, list(value))

group_obj2 = groupby(a, key=lambda x: x<3)
for key,value in group_obj2:
    print(key, list(value))

persons = [{'name': 'Tim', 'age':25}, {'name': 'Dan', 'age': 25},
            {'name': 'Lista', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj3 = groupby(persons, key=lambda x: x['age'])
for key,value in group_obj3:
    print(key, list(value))

print("###### infinite ######")
from itertools import count, cycle, repeat
for i in count(10): # creates an infinite loop that starts at 10, and adds 1 for every repetition
    print(i)
    if i == 15:
        break
a = [1,2,3]
#for j in cycle(a): # will cycle infinitely through the list until a condition is met (i.e 1,2,3,1,2,3,1,2,3,1,2,3...)
#    print(j)
for k in repeat(1, 4): # will make a infinite loop that will print 1, until a stop point (4 in this case). So will repeat 1, four times.
    print(k)
