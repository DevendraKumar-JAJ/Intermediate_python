myList=[0]*5
print(myList)

myList2=myList
# both mylist1 and 2 refers same memory address so  performing task on any list refers to other list...

myList2.append('A')

print(myList2)
print(myList)

list1=[1,2,3,5,4,6,8,7]
print(list1) #[1, 2, 3, 5, 4, 6, 8, 7]
print(*list1) #1 2 3 5 4 6 8 7

print(list1+[2,3]) #[1, 2, 3, 5, 4, 6, 8, 7, 2, 3]
# print(list1-[2])err

list1.insert(100,5) # at last index 
print(list1)

print(list1.pop(0))
print(list1)

list1 = [1, 2, 3, 4, 5]
del list1[0]
print(list1)  # Output: [2, 3, 4, 5]

