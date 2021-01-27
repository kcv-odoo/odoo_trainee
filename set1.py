empty_set = set()
some_set = {1, 1, 2, 2, 3, 4}
# invalid_set = {[1], 1}  #typeeror
valid_set = {(1,), 1}  
filled_set = some_set
filled_set.add(5)
filled_set.add(5) #set not allow duplication
other_set = {3,4,5,6}
filled_set & other_set  #common in both var intersection
filled_set | other_set   #union contain all ele from both
print({1, 2, 3, 4} - {2, 3, 5})  #{1, 4}(diff)ele from positive which not in second set
print({1, 2, 3, 4} ^ {2, 3, 5} ) #(symmetric diff) unique ele from both set
print({1, 2} >= {1, 2, 3})  #check set on the left is superset of right
print({1, 2} <= {1, 2, 3}) #check set on left is subset of right set
filled_set = some_set.copy()  
filled_set is some_set   
