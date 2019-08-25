mystring='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)

print(mylist)
# ['h', 'e', 'l', 'l', 'o']

mylist = [letter for letter in mystring]
print(mylist)
# ['h', 'e', 'l', 'l', 'o']

mylist=[x for x in range(0,11)]
print(mylist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist=[x**2 for x in range(0,11)]
print(mylist)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist=[x for x in range(0,11) if x%2==0]
print(mylist)
# [0, 2, 4, 6, 8, 10]

cesius=[0, 10, 20, 30]
faren=[((9/5)*temp + 32) for temp in cesius]
print(faren)
# [32.0, 50.0, 68.0, 86.0]

faren =[]
for temp in cesius:
    faren.append((9/5)*temp + 32)
print(faren)
# [32.0, 50.0, 68.0, 86.0]

res=[x if x%2==0 else 'odd' for x in range(0,11)]
print(res)
# [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd', 10]

mylist = []
for x in [2, 3, 4]:
    for y in [10, 20, 30]:
        mylist.append(x*y)

print(mylist)
# [20, 40, 60, 30, 60, 90, 40, 80, 120]

mylist=[x*y for x in [2,4,6] for y in [1,2,3]]
print(mylist)
# [2, 4, 6, 4, 8, 12, 6, 12, 18]
