import random
def solution(N):
    sum = 0
    result = []
    oddValue = random.randint(1,101)
    print(oddValue)
    mod = N
    isEven = N%2==1
    print(isEven)
    if(isEven):
        mod = N-1
        result.append(oddValue)

    i = 0
    while i < (mod/2):
        randNum = random.randint(1,101)
        result.append(randNum)
        result.append(-1*randNum)

        i += 1

    if(isEven):
        result[random.randint(0, len(result)-1)] -= oddValue

    return result


print(solution(5))
