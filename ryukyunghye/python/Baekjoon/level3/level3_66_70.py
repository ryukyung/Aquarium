# [10820] 문자열 분석
while True:
    try:
        text = input()
        lower = sum(i.islower() for i in text)
        upper = sum(i.isupper() for i in text)
        number = sum(i.isdigit() for i in text)
        space = sum(i.isspace() for i in text)
        print(lower, upper, number, space)
    except:
        break

# [2743] 단어 길이 재기
text = input()
print(len(text))

# [11655] ROT13
S = input()
rot = ''
for s in S:
    if 'A' <= s <= 'Z':
        rot += chr((ord(s)+13) if s <= 'M' else ord(s)-13)
    elif 'a' <= s <= 'z':
        rot += chr((ord(s)+13) if s <= 'm' else ord(s)-13)
    else:
        rot += s
print(rot)

# [10824] 네수
a, b, c, d = map(str, input().split())
AB = int(a+b)
CD = int(c+d)
print(AB+CD)

# [11656] 접미사 배열
s = input()
sList = []
for _ in s:
    sList.append(s)
    s = s[1:]
for i in sorted(sList):
    print(i)
