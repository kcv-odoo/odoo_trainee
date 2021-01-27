from functools import reduce



print((lambda x, y: x ** 2 + y ** 2)(2, 1))
print(list(map(len, [[1,2],[3,4],[5,6,7,8,9]])))
print(list(filter(lambda x: x>5, [3,4,5,6,7])))
print(reduce(lambda x,y: x+y,[1,2,3,4,5,6]))

