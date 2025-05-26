from collections import Counter
from collections import namedtuple
from collections import OrderedDict
import collections

a='45555adfaaaaaffffdddd4'

eachChar=Counter(a)
print(eachChar)

print(f'There are {eachChar['a']} a and {eachChar['d']} d.')

print(eachChar.most_common(1)[0][0]) #a
print(list(eachChar.elements()))



# 
# 
# named tuple

Point=namedtuple('Point','x,y,z')
# pt=Point(1,5)# arg missing
pt=Point(1,5,2)
print(pt.x,pt.y)
# pt.x=7 # error like tuple 
# 
# 

dictt=OrderedDict()
dictt[0]=1
dictt[1]=2
dictt[2]=3
dictt[3]=4
dictt[4]=5
dictt[5]=6
print(dictt) #OrderedDict({0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6})

dictt=collections.defaultdict(int)
dictt['a']=1
dictt['b']=2

print(dictt)
print(dictt['c']) #0

d=collections.deque()
d.append(1)
d.append(2)
d.appendleft(3)

print(d)
d.pop()
d.popleft()
print(d)

d.extend([4,5,6])
d.extendleft([5,4,3])
print(d)