# def hello_decorator(func): 
  
#     # inner1 is a Wrapper function in  
#     # which the argument is called 
      
#     # inner function can access the outer local 
#     # functions like in this case "func" 
#     def inner1(): 
#         print("Hello, this is before function execution") 
  
#         # calling the actual function now 
#         # inside the wrapper function. 
#         func() 
  
#         print("This is after function execution") 
          
#     return inner1 
  
  
# # defining a function, to be called inside wrapper 
# def function_to_be_used(): 
#     print("This is inside the function !!") 
  
  
# # passing 'function_to_be_used' inside the 
# # decorator to control its behavior 
# function_to_be_used = hello_decorator(function_to_be_used) 
  
  
# # calling the function 
# function_to_be_used() 



from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())                 # Can you buy me a beer?
print(say(say_please=True))