filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) 
for i in our_iterable:
    print(i)  
# our_iterable[1]   #we cannot address ele by index
our_iterator = iter(our_iterable)  #return object which can be iterated
next(our_iterator)  #get next ele and start iteration where it is left-off
next(our_iterator)  
next(our_iterator) 
# next(our_iterator)  #stopiteration
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)
    #you can call ele of iterable by calling list()
#you can call ele of iterable by calling list()
print(list(our_iterable))  #return ['one','two','three']
print(list(our_iterator)) #return [] because its state is saved
