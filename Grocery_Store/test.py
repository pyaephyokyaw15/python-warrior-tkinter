list1 = ['hello', 'world']
print(enumerate(list1))

for num, item in enumerate(list1):
    print(num)
    print(item)


for item in enumerate(list1):
    print(item)
