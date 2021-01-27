#differance between == and is
a = [1,2,3,4]
b = [1,2,3,4]
c = a
print(a==b)
print(a is b)
print(a is c)
print(a==c)
#print format
print(f"His answer is {a is b}")
print("a==b is {} and a is b {} ".format(a==b,a is b))
print("yes" if(0>1) else "no")
#list and its operations
li = []
oh_li = [4,6,8]
#list and its function
#append to insert element in list list_name.append()
li.append(1)
li.append(2)
li.append(5)
print(li)
#pop to remove element from list pop(index(optional)) if index is not given it'll pop last element
li.pop()
li.append(4)
li.append(7)
li.pop(2)
li.append(5)
li.pop(-2)
print(li)
#access element of list like array list_name[index]
print(li[1])
print(li[0])
print(li[-2])
#list sliceing list_name[start_index(0):end_index(-1):increament(1)] default value if its not given by user
li.append(8)
li.append(9)
print(li)
print(li[1:3])
print(li[:-1])
print(li[::2])
#del for deleting list or portion of list or element f list del list_name[index]
del li[-1]
print([li])
#remove for removing first occerance of element in list list_name.remove[value]
li.append(5)
li.remove(5)
print(li)
#insert element at specific index list_name.insert(index,value)
li.insert(1,6)
print(li)
#+operater concatenate two list and return new list instead concatenate we can also use extend to concatenate list 
#list_name.extend(other_list_name) exend concatenate second list to first list and return nothing
li1 = li + oh_li
li2 = li.extend(oh_li)
print(li1)
print(li)
print(li2)
#in used for check whether element is in the list or not and accoringly return boolean value 
print(2 in li)
print(7 in li)
#len to return length of list len(list_name)
print(len(li))


#tuple 
#tuple are like list but immutable we can not modify its value  after intilazation 
#tuple create using round bracket or tuple() function
tu = (1,2,3)
tu1 = tuple(li)
tu2= () #empty tuple
print(type(tu2)) # type is use for getting type of variable
print(id(tu2))   #id return address of memory where variable point or value of variable is store
#we can unpack tuple or list into variable
a,*b,c = li
x,*y = tu
print(f"a = {a} b = {b} and  c = {c}")
print("x = {} and y = {}".format(x,y))
#we can perform indexing slicing copying and len fn on tuple as we perform in list 

#DICTIONARIES
#dictionariers store  mapping from key to value 
#it define using { } 
# in dictionary keys are immutable cause system can convert keys  into hash value for simple look ups 
# immutable data like any primitive data like int float char and string tuple etc 
#and value can be any thing mutable or immutable
dict1 = {} #empty dict
dict2 = {1:"first",2:"second"} 
lst1 = list(dict2.keys())
lst2 = list(dict2.values())
print(lst1)
print(lst2)
print(dict2[2])
dict2[3] = "third"
#in for checking key is in the dict or not return boolean value accordingly
print(1 in dict2)
#get fn for avoid non exiting key error it return none  instead giving error
print(dict2[1])
print(dict2.get(4)) 
del dict2[2]
print(dict2)
#setdefault for give a default value to key if key not already in dict 
dict2.setdefault(2,"second")
print(dict2)

