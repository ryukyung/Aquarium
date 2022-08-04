# [11047] 동전0
kindOfCoin, makeMoney = map(int, input().split())
coinList = []
for _ in range(kindOfCoin):
    coinList.append(int(input()))

result = 0
for i in range(kindOfCoin-1, -1, -1):
    if makeMoney == 0:
        break
    if coinList[i] > makeMoney:
        continue
    result += makeMoney // coinList[i]
    makeMoney %= coinList[i]
print(result)
