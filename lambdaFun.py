'''
- Lambda Function: Defined using the lambda keyword.
- Lambda Function: Limited to a single expression.
- Lambda Function: Implicitly returns the result of the expression.
- Lambda Function: Limited to a fixed number of arguments.
- Lambda Function: Ideal for simple, one-time use cases, such as event handling, data processing, or as higher-order functions.

'''

#  print n * 10

import functools
mul10=lambda x:x*10
x=int(input('Enter X: '))
print (x)
print(f"{x}*10 = {mul10(x)}")
# 
# 

l1=[(1,2),(15,1),(5,-1),(10,4)]

print(sorted(l1)) #[(1, 2), (5, -1), (10, 4), (15, 1)]
# based on first member tuple
print(sorted(l1,key=lambda x:x[0])) #[(1, 2), (5, -1), (10, 4), (15, 1)]


# based on second member tuple
print(sorted(l1,key= lambda x:x[1])) #[(5, -1), (15, 1), (1, 2), (10, 4)]

#based on second ele - first ele whose smaller.....
print(sorted(l1,key= lambda x:x[1]-x[0]))  #[(15, 1), (5, -1), (10, 4), (1, 2)] 

a=range(11)

# multiple of each ele in list a by 2 
b=list(map(lambda x:x*2,a)) 
print(b) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 

# same thing
print([x*2 for x in a ]) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#all even number in a list 
b=list(filter(lambda x:x%2==0,a)) # return value based on condtition true,,
print(b) # [0, 2, 4, 6, 8, 10]
#same 


#  sum of all ele in a list 
b=functools.reduce(lambda x,y:x+y,a)
print(b) #55  | 0-10

# print(help(functools)) 