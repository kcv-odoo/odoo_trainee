try:
    raise IndexError("This is an index error") #raise keyword to raise error
except IndexError as e:
    pass                 
except (TypeError, NameError): #multiple exception handle
    pass                 
else:                   
    print("All good!")   
finally:                
    print("We can clean up resources here")
