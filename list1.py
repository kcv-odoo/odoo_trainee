li = []
other_li = [4, 5, 6]
li.append(1)   
li.append(2) 
li.append(3)
li.append(4) #add ele at last in list
li.pop() 
del li[2]  #delete the ele at index 2
li.remove(2) #delete the ele 2
print(li[0]) #accessing list ele through indexing
print(other_li, li)
print(li + other_li )
li.extend(other_li) #concatenate list 
print(2 in li)  #check existence in a list with in
