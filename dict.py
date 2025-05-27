# dict is a unorderd , mutable, do not allow duplicates

dict1={'name':'Devendra Kr','Roll_num':23,}
print(dict1) 
dict1={'a':1,'z':2,'c':3,'s':3,'d':0}
print(dict1)
dict2=dict(name='DevEndra',Roll_Num=23) # through dictonary constructor 
print(dict2['name'], dict2['Roll_Num'])

dict2['name']='Rahul' #mutable
print(dict2['name'])

print(dict1.popitem()) # ('d',0) last removed ele | return a typle  | no arg
print(dict1.pop('a')) # pop item where key is a. | at least one arg| return 1 or 0 | 1 if poped ,0 if not poped 
print(dict1)

print(dict1.keys()) # A list of keys
for key in dict1.keys():
  print(key,end=' ')
  
print('\n',dict1.values()) # A list of values
for value in dict1.values():
  print(value,end=' ')
  
for key,value in dict1.items():
  print(f'\n{key }:{value}',end='')
  
dict2_cpy=dict2
dict2_cpy['email']='dkumar@gmail.com'
print('\n',dict2) # both will changed 
print(dict2_cpy)

dict2_cpy=dict2.copy()
dict2_cpy['email']='rahul@gmail.com'
print('\n',dict2) # only dict2_cpy  will changed 
print(dict2_cpy)

#  also we can do 
dict2_cpy=dict(dict2)
dict2_cpy['email']='rahul@gmail.com'
print('\n',dict2) # only dict2_cpy  will changed 
print(dict2_cpy)


# tuple as dict 
tuple1=1,2,3
dict3={tuple1:5}
print(dict3)
print(dict3[tuple1])
# print(dict3[tuple1[0]]) #  Error 
list1=[1,2,3]
# dict3={list1:5} # error list not as a key | beacuse list mutable
