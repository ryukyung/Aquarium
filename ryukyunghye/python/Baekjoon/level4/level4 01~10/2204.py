# [2204] 도비의 난독증 테스트
while True:
    testCase = int(input())
    wordList = []
    if testCase == 0:
        break
    for _ in range(testCase):
        wordList.append(input())
    wordList.sort(key=str.lower)
    print(wordList[0])
