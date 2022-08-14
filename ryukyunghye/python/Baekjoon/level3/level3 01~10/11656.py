# [11656] 접미사 배열
s = input()
sList = []
for _ in s:
    sList.append(s)
    s = s[1:]
for i in sorted(sList):
    print(i)
