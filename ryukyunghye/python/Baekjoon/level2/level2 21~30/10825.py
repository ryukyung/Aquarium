# [10825] 국영수
import sys
n = int(sys.stdin.readline())
data = [list(sys.stdin.readline().split()) for _ in range(n)]
data.sort(key=lambda a:  (-int(a[1]), int(a[2]), -int(a[3]), a[0]))
for i in data:
    sys.stdout.write(str(i[0])+'\n')
