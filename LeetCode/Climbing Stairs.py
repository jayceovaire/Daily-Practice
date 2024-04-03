def climbStairs(n:int) -> int:

    if n == 1:
        return 1
    elif n == 2:
        return 2

    stepOne = [0] * (n + 1)
    #print(stepOne)
    stepOne[1] = 1
    stepOne[2] = 2
    #print(stepOne)
    for i in range(3, n+1):
        #print(stepOne[i])
        stepOne[i] = stepOne[i - 1] + stepOne[i - 2]
        #print(stepOne)


    return stepOne[n]



def climbTwo(n: int) -> int:

    ways = [1, 1, 2]
    prev = ways[2]

    for i in range(3, n + 1):
        current = ways[i - 1] + ways[i - 2]
        ways.append(current)




