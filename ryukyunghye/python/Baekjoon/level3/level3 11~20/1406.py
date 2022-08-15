# [1406] 에디터
import sys
string = list(input())
stringList = []
n = int(input())
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "L" and string:
        stringList.append(string.pop())
    elif command[0] == "D" and stringList:
        string.append(stringList.pop())
    elif command[0] == "B" and string:
        string.pop()
    elif command[0] == "P":
        string.append(command[1])

print("".join(string + list(reversed(stringList))))
