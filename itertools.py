import itertools
from timeit import default_timer as Timer
import operator
a=[1,2]
b=[3,4]

prod=itertools.product(a,b ) # cartion product 
print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)]

a=[0,1,2,3]
prem=itertools.permutations(a,4)
print(list(prem))

passAll=list(prem)

start=Timer()
for x in passAll:
  if(x==(9,8,7,6)):
    print("pass Creacked.",passAll.index(x))
    break
stop=Timer()

print(f'Sec: {stop-start:.5f}')
prem=itertools.combinations(a,4)
print(list(prem))

# 
# 
# 
# 
a=[1,2,3,4,5,6,7,8,9,10]
#  factorial of all 

b=itertools.accumulate(a,func=operator.mul)
print(list(b)) #[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
# 
# 
# 
def  smallThan3(x):
  return x%2==0

a=range(11)
b=itertools.groupby(a,key=smallThan3)
for key,val in b:
  print(list(val),end=' ')
  if key:
    print('Even')
  else:
    print('Odd')

# lambda fun is same as callback fun in js

a=range(11) #        ______ lambda FUn______
b=itertools.groupby(a,key=lambda x:x%2==0)
for key,val in b:
  print(list(val),end=' ')
  if key:
    print('Even')
  else:
    print('Odd')


person=[{'name':'Dev','age':20},{'name':'Dev','age':35},{'name':'Dev','age':30},{'name':'Dev','age':25},{'name':'Dev','age':21}]

persG= itertools.groupby(person,key=lambda x: x['age']>29)

for key,val in persG:
  if key:
    print(f'List of persons whoes age is 30 or more : \n\t{list(val)}')
    
    
# 
# 

for i in itertools.count(0,2,): # this take only starting point an step like 10 is starting and step is 2
  print (i,end=" ")
  if i==20:
    break