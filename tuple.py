# tuple is Ordered , immutable , allow duplicates and smaller than list in size.
import sys
import timeit
tuple1='Max',20,False #typle

print(type(tuple1))

tuple2=('max')#string type
tuple3=('max',)#tuple
tuple4=('ram','god')#tuple
print(type(tuple2),type(tuple3),type(tuple4))
print(tuple4[0])

# tuple4[0]='sita' not possible | tuple is immutable..
tuple5=(['ram',18]) #list
print(type(tuple5))

tuple6=tuple([8,5,7]) # a list typecast in tuple...

if(8 in tuple6):
  print('Yes ')


print(tuple4.count('ram')) # cout ram in list 
print(tuple4.count('sita'))

tuple8=tuple(list(tuple4))
print(type(tuple8))
print(tuple1[0:2]) # ('max',20)
print(tuple1[::-1]) # reverse of tuple1


name,iss=tuple4
print(f'{name} is {iss}.')

strr,intt,boll=tuple1
print(f'str : {strr}, int {intt}, bool {boll}')
# strr,intt=tuple1 # err : too many values to unpack
print(f'str : {strr}, int {intt}')
tuple9='Name',1,2,5,8,9,'Ram'

i1,*i2=tuple9 #i1 is a str and i2 is a list
#  * variable never in start make sure may a single variable before * variable
print(i1,i2)

tuple10=(1,2,3,4,5)
list1=[1,2,3,4,5]

print('tuple: len 5 :',sys.getsizeof(tuple10),'bytes')
print('list | len 5',sys.getsizeof(list1),'bytes')

print('Times taken by a tuple init 1m times: ',timeit.timeit(stmt='(1,2,3,4,5)',number=1000000))
print('Times taken by a list init 1m times: ',timeit.timeit(stmt='[1,2,3,4,5]',number=1000000))