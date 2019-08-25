
x=0
while x<5:
    print(f'x is {x}')
    x+=1
else:
    print('k')

x=[1,2,3]
for item in x:
    #comment
    pass

print("end")

mystring='Sammy'
for letter in mystring:
    if(letter =='a'):
        continue
    print(letter)

mystring='Sammy'
for letter in mystring:
    if(letter =='a'):
        break
    print(letter)
x=0

while x<5:

    if x == 2:
        break
    print(x)
    x+=1
