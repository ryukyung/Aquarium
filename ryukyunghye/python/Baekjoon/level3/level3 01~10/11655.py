# [11655] ROT13
S = input()
rot = ''
for s in S:
    if 'A' <= s <= 'Z':
        # 참일 때  if 조건식 else 거짓일때
        rot += chr((ord(s)+13) if s <= 'M' else ord(s)-13)
    elif 'a' <= s <= 'z':
        rot += chr((ord(s)+13) if s <= 'm' else ord(s)-13)
    else:
        rot += s
print(rot)
