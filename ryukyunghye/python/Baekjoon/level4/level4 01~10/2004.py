# [2004] 조합 0의 개수
'''
nCr = n!/(n-r)!r!
2의 지수 = n!의 2의 지수 - (n-r)!의 2의 지수 - r!의 2의 지수
5의 지수 = n!의 5의 지수 - (n-r)!의 5의 지수 - r!의 5의 지수
2의 지수와 5의 지수 중 작은 값을 고르면 된다
-> result2 += n//2, result5 += n//5: 시간초과 발생
'''
n, m = map(int, input().split())


def twoCount(n):
    result2 = 0
    while n != 0:
        n = n//2
        result2 += n
    return result2


def fiveCount(n):
    result5 = 0
    while n != 0:
        n = n//5
        result5 += n
    return result5


print(min(twoCount(n)-twoCount(n-m)-twoCount(m),
      fiveCount(n)-fiveCount(n-m)-fiveCount(m)))
