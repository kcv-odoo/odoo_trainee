tup = (1, 2, 3)
tup[0]     
# tup[0] = 3  #immutable hence give typeerror
print(type((1)) )  
print(type((1,)) )
print(type(()))
print(len(tup))
print(tup + (4, 5, 6))
print(tup[:2])
print(3 in tup)
a, b, c = (1, 2, 3)  #unpacking
print(a,b,c)
a, *b, c = (1, 2, 3, 4) #this would look like 1,[2,3],4
print(a,b,c)
d, e, f = 4, 5, 6 #leave them without square bracket by default it will tuple
print(d,e,f)  
