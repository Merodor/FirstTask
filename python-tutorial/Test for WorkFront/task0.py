mylist=[-6, -100,100]

def solution(A):
    result = None
    sortedList = sorted(list(dict.fromkeys(A)))

    print(sortedList)
    for num in sortedList:
        if(num%4==0):
            result=num
            break
    return result

print(solution(mylist))
