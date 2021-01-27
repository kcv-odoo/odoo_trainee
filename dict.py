empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
# invalid_dict = {[1,2,3]: "123"}   #key can not be mutable
valid_dict = {(1,2,3):[1,2,3]} #this is ok bcoz tuple is immutable
print(filled_dict["one"]) 
print(list(filled_dict.keys()) )
# filled_dict["four"] #might u get typeeeror
print(filled_dict.get('one'))  #get value according key given
print(filled_dict.setdefault("five", 6) )  #set key-value if given key not there 
print(filled_dict.update({"four":4})) #adding to dictionary
del filled_dict["one"] #delete
