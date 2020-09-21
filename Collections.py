# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
print("###### Counter ######")
from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common(3))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0]) #-> most common element in our string
print(my_counter.elements())
print(list(my_counter.elements()))

print("###### namedtuple ######")
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

print("###### OrderedDict ######")
from collections import OrderedDict # OrderedDict is used in python versions <3.6 as from 3,6 onwards, dicts remember the order by default.
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)
ordered_dict2 = OrderedDict()
ordered_dict2['b'] = 2
ordered_dict2['c'] = 3
ordered_dict2['d'] = 4
ordered_dict2['a'] = 1
print(ordered_dict2)

print("###### defaultdict ######")
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['a'])
print(d['b'])
print(d['c'])
print(d['z']) # -> Will return default value for an integer (0) if no element is found.

d2 = defaultdict(float)
d2['a'] = 1.1
d2['b'] = 2.3
d2['c'] = 3.5
print(d2['z'])

d3 = defaultdict(list)
d3['a'] = 1
d3['b'] = 2
print(d3['z']) # -> Will return an empty list if the dictionary key doesn't exist.

d4 = {}
d4['a'] = 1
d4['b'] = 2
#print(d4['c']) # -> If we don't use defaultdict and try to print a non-exists dict key, it will raise error.

print("###### Deque ######") # stands for Double ended queue
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([-0,-1,-2])
print(d)
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)
