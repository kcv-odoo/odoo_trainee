"""import json
with open("demo.txt") as f:
    for line in f:
        print(line)
content = {"aa": 1,"bb":2}
with open("demo.txt","a") as fl:
   fl.write("\n" +str(content))
with open("demo.txt","w+") as f:
    f.write(json.dumps(content))
with open("demo.txt","r+") as f:
    abc = json.load(f)
print(abc)
"""
#iterator
list1 = [1,3,5,8]
itr1 = iter(list1)
print(next(itr1))
print(itr1.__next__())
count = 0
for i in itr1:
    print(i)
    print(itr1.__next__())
    count += 1
print(count)
def keyarg(**abc):
    return abc
abc = keyarg(big="one",foot="two")
print(abc.keys())
