# [10808] 알파벳 개수
s = input()
alphabet = [0] * 26
for i in s:
    alphabet[ord(i)-97] += 1
print(*alphabet)
