mylist=[-10,1,2,3,4,4,0,5, 10]
mylist=[1,2,3]

def solution(A):
    result = 0
    sortedList = sorted(list(dict.fromkeys(A)))
    index = 0
    for num in sortedList:
        if num < 1:
            index += 1
        else:
            break

    for el1, el2 in enumerate(sortedList[index:], 1):
        print(f"{el1, el2}")
        if(el1!=el2):
            result = el1
            break

    if(result == 0):
        result = sortedList[-1] + 1

    if(result < 1):
        result = 1

    return result


print(solution(mylist))

#
# def solution(A):
#     # write your code in Python 3.6
#
#     sorted_A = sorted(A)
#     print(sorted_A)
#
#     highest = 0
#     for i in range(len(sorted_A) - 1):
#         if sorted_A[i] < 0:
#             continue
#         if sorted_A[i+1] - sorted_A[i] > 1:
#             highest = sorted_A[i]
#             break
#
#     if not highest:
#         highest = sorted_A[-1]
#
#     if highest < 0:
#         highest = 0
#
#     return highest + 1
#
# print(solution(mylist))
