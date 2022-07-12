# [2447] 별 찍기 - 10
n = int(input())


def printStar(x):
    if x == 3:
        return ['***', '* *', '***']
    array = printStar(x//3)
    stars = []
    for i in array:
        stars.append(i*3)
    for i in array:
        stars.append(i+' '*(x//3)+i)
    for i in array:
        stars.append(i*3)
    return stars


print('\n'.join(printStar(n)))
