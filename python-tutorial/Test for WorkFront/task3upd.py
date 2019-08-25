myList = [4,5,2,3,4]
myList1 = [3,4,5,4]
myList2 = [1,2,3,4,5,6,7]

def solution(A):
    def isCutable(i):
        prevThrees = []
        nextThrees = []

        if(i > 0):
            prevThrees = A[:i]

        if(i < len(A)-1):
            nextThrees = A[i+1:]

        print(prevThrees + [f"-"] + nextThrees)
        print(sorted(prevThrees + nextThrees))
        print(prevThrees + nextThrees == sorted(prevThrees + nextThrees))
        return prevThrees + nextThrees == sorted(prevThrees + nextThrees)

    i = 0
    result = 0
    while i < len(A):
        if isCutable(i):
            result += 1
        i+=1


    return result



print(solution(myList1))
