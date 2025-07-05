from timeit import  default_timer as timer
str1='"I am a student"' # contain duble quates
str2="I'm a student" # contain single quates
str3='''Hello!
 I am "Devendra Kr ".''' # multiline string
print(str3) 

str4='I\'m Devendra Kumar and,\n I am \"18\" yrs old.\n' # escape seq used
print(str4)
str5='Hello World'
print(*str5) #  H e l l o   W o r l d

for charr in str5:     # same as above
  print(charr,end=' ') # H e l l o   W o r l d
  
charr=str5[0]
print('\n',charr)
# str5[0]='w' #error imutable

slcedStr=str5[6::1] # World
print(slcedStr)
slcedStr=str5[:-6:-1] # dlroW  | reverse
print(slcedStr)

print(str5+str5) #Hello WorldHello World
# print(str4+1) # error
# print(1+str4) # error
# print(1-str4) # error
# print(str4-1) # error
print(str5*3) # Hello WorldHello WorldHello World
# print(str5/3) # error


# every letter verticaly
for char in str5:
  # print(char)
  print(char ,end='\n') # both are same
  
str6="     Hello    "
print(str6) # (     Hello     )  still whitespace
print(str6.strip()) # Hello | without white spaces
print(str6.upper())
print(str6.lower())
print(str6.strip().capitalize()) # Hello | without whitespace 
print(str6.casefold()) # if upper than lower | if lower than upper
print(str6.rstrip()) # right whitespace strip
print(str6.lstrip()) # left whitespace strip
print(str6.replace('Hello','Hiii')) # replace

str7="Hello world, I'm Devendra."

list1=str7.split() # ['Hello', 'world,', "I'm", 'Devendra.'] | each world 
print(list1)
print(list(str7)) #['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ',', ' ', 'I', "'", 'm', ' ', 'D', 'e', 'v', 'e', 'n', 'd', 'r', 'a', '.'] | each character
print(str7.split(','))  #['Hello world', " I'm Devendra."] | two seprate string divided based on comma

print(''.join(str7.split(','))) #Hello world I'm Devendra. | first split based on comma then agin join all with a empty string

str8='1'
list2=list(str8*5)
print(list2) # ['1', '1', '1', '1', '1']

list3=['1']*500000

# 
start=timer()
str9=''
for char in list3:
  str9+=char
stop=timer()
print(f'Init time [loop] : {stop-start:.2f}') #15.2932 seconds to do this work done
# 

start = timer()
str9=''.join(list3)
stop=timer()
print(f'Init time [join()]: {stop-start:.2f}')# 0.0053 seconds to do this work done 

# # how long margin 

str10='0 is smaller than %s'%str8 
print(str10) # 0 is smaller than 1
str10='0 is smaller than '+str8 
print(str10) # 0 is smaller than 1
str10=f'0 is smaller than {str8}'
print(str10) # 0 is smaller than 1
str10='0 is smaller than {} and {}'.format(str8,str8)
print(str10) # 0 is smaller than 1

