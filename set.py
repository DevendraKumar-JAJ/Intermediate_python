# set  mutable ,no duplicates,unorderd
set1={1,2,3,9,8,7}
print(set1) # {1, 2, 3, 7, 8, 9} unorderd
set2=set('Hello')
print(set2) #{'H', 'e', 'l', 'o'} no duplicates 

set3={} # it is an empty dictionary
print(type(set3)) # dict
set4=set() # this an empty set
print(type(set4)) # dict

set5=set()
set5.add(4)
set5.add(4j)
set5.add(True)
set5.add('Hello')
print(set5) #{True, 4, 4j, 'Hello'}

# set5.remove(5) # key error
# so in set key is same as value
set5.remove(True)
print(set5) #{4, 4j, 'Hello'}

print(set5)
print(set5.pop()) # deleting item from first index
print(set5.pop()) # deleting item from first index
print(set5) #{4j} | {'Hello'} sometime different 

set6={'Hi','Ram','Hii','Shyam'}
print(set6) #{'Hi', 'Shyam', 'Hii', 'Ram'}   | {'Hi', 'Hii', 'Shyam', 'Ram'} | {'Hii', 'Hi', 'Ram', 'Shyam'} may output different

if('Ram' in set6):
  print('Yes present.')
else:
  print('Not ')
  
  
odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

# Unioun or Concat both ele who are unique in all sets

# union=evens+odds # err
union=odds|evens
print(union) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# intersection both who  present in both set
intersect=odds&evens
print(intersect) #set() empty set

union=evens.union(odds.union(primes))
print(union) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

intersect=evens.intersection(odds)
print(intersect) #set()
evens.add(10)
odds.add(10)
intersect=evens.intersection(odds)
print(intersect) #{10}

# prime number which is odd
print(primes.intersection(odds)) #{3, 5, 7}
print(odds.intersection(primes)) # same res

# prime num which is even

print(evens.intersection(primes))


setA={1,2,3,4,5,6,7,8,9}
setB={1,3,5,7,9,11,13,15}
# print a ele which present once  in setA 
print(setA.difference(setB)) # {8, 2, 4, 6}
# print a ele which present once  in setB
print(setB.difference(setA)) #{11, 13, 15}

# unique number which present once in either setA or setB
print(setA.symmetric_difference(setB)) #{2, 4, 6, 8, 11, 13, 15}
print(setB.symmetric_difference(setA)) # same


setA.update(setB)
print(setA) # setA becomes  {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15}

setA.difference_update(setB)
print(setA) #setA becomes {2, 4, 6, 8}


setA={1,2,3,4,5,6,7,8,9}
setB={1,3,5,7,9,11,13,15}
setA.intersection_update(setB)
print(setA) #setA becomes {1, 3, 5, 7, 9}

print(setA.issubset(setB)) # true all value of setA present in setB
print(setB.issubset(setA)) # false all value of setB not  present in setA
print(setA.issuperset(setB)) # same as above both have same meaning
print(setA.isdisjoint(setB)) # false | is setA ele are totaly differ than setB |
print(setB.isdisjoint(setA)) # false | is setB ele are totaly differ than setA |

setA={1,2,3}
setB={4,5,6}
print(setA.isdisjoint(setB)) # true

setA=setB
setB.add('A')

print(setA) #{'A', 4, 5, 6}
print(setB) #{'A', 4, 5, 6} | mutable

setA=setB.copy()
setA.add('B')
print(setA) #{'A', 4, 5, 6, 'B'}
print(setB) #{'A', 4, 5, 6} 

setA=set(setB)
setA.add('C')
print(setA) #{'A', 4, 5, 6, 'C'}
print(setB) #{'A', 4, 5, 6} 

#frozenSet | imutable version of normal set
# setC=frozenset(1,2.3,4) # error | only one arg
setC=frozenset([1,2,3,4])
setD=frozenset([5,6,7,8])

print(setC,setD)

print(setD.union(setC)) # return frozenset 


setA=set([1,2,3,4]) #normal set
setC=frozenset([2,1]) #frozenset
setA.add(1)
# setC.add(2) # 'frozenset' object has no attribute 'add'
print(setA,setC)

# print(setA+setB) #err
print(setA-setB) #{1, 2, 3}
# print(setA*setB) #err
# print(setA/setB) #err
