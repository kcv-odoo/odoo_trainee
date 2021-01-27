def varargs(*args):
    return args
print(varargs(1, 2, 3))

def keyword_args(**kwargs): #keyword arg pass as in form of dictionary
    return kwargs
print(keyword_args(big='foot',loch='ness'))