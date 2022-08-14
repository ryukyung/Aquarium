# [10809] 알파벳 찾기
word = input()
alphabet = list(range(97, 97+26))
for i in alphabet:
    print(word.find(chr(i)))
