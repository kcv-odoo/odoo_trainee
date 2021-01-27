def double_numbers(iterable):
    for i in iterable:
        yield i+2   #yield(is what make generator) method same works as return but it can save 
        # the state of varibale and when fun call its execution starts from where it is left off

for i in double_numbers(range(1, 2500)):  # `range` is a generator.
    print(i)
    if i >= 15:
        break