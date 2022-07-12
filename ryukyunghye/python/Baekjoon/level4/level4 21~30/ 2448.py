# [2448] 별 찍기 - 11
n = int(input())


def printStar(x):
    if x == 3:
        return ['  *  ', ' * * ', '*****']
    array = printStar(x//2)
    stars = []
    for i in array:
        stars.append(' '*(x//2)+i+' '*(x//2))
    for i in array:
        stars.append(i+' '+i)
    return stars


print('\n'.join(printStar(n)))
