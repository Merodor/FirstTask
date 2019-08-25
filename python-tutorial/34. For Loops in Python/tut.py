myList=[6,7,8,1,2,3,4,5]
# for i in myList:
#     print(i)
#
# for i in myList[1:]:
#     print(f"hello {i%2==0} {i}")

sum=0
for item in myList:
    sum+=1

print(sum)

mystring="Hello world"
fromatedtext=''
for leeter in mystring:
    fromatedtext += leeter + "\t"

print(fromatedtext)

print(mystring.replace("", "\t").replace("\t"+mystring[0], mystring[0]))
tup=(1,2,3,4)
for item in tup:
    print(item)

mylist=[(1,2),(3,4),(5,6),(8,9)]
print(len(mylist))

for item in mylist:
    print(item)

for (a,b) in mylist:
    print(f"hello {a} {b}")

d={'k1':1,'k2':2, 'k3':3}
for item in d:
    print(item)

for key,v in d.items():
    print(v)
