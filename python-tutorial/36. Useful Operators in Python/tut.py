mylist=[1,2,3]
for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(3,100,4):
    print(num)

print(list(range(2,100,5)))

index_count=0
for letter in 'abcde':
    print(f'index {index_count} the letter is {letter}')
    index_count+=1

index_count=0
word='abcde'
for letter in word:
    print(word[index_count])
    index_count+=1

word='abcde'
for item in enumerate(word):
        print(item)

word='abcde'
for index,letter in enumerate(word):
        print(f'{index}' +'\t' +letter+'\n')

mylist1=[1,2,3,4]
mylist2=['a','b']
mylist3=zip(mylist1,mylist2)
print(mylist3) #baka

for item in mylist3:
    print(item)

print(list(mylist3))

print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('a' in 'hola world')
print('mykey' in {'mykey':2345})

d = {'mykey':345}
print(345 in d.keys())

mylist=[10,20,30,40]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist=[1,2,3,4,5,6,7,8,9]
randomlist=shuffle(mylist)
print(randomlist)
print(type(randomlist))
from random import randint
print(randint(0,100))
mynum=randint(0,100)
print(mynum)
#not working cos no input here
result =input('Enter number: ')
print(type(result)) #type is string
print(float(result)) # return 20.0
print(int(result)) # return 20
