# [1517] 버블 소트
def mergeSort(start, end):
    global swapCount, A

    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        startPoint, midPoint = start, mid + 1
        temp = []

        while startPoint <= mid and midPoint <= end:
            if A[startPoint] <= A[midPoint]:
                temp.append(A[startPoint])
                startPoint += 1
            else:
                temp.append(A[midPoint])
                midPoint += 1
                swapCount += (mid - startPoint + 1)

        if startPoint <= mid:
            temp = temp + A[startPoint:mid + 1]
        if midPoint <= end:
            temp = temp + A[midPoint:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]


swapCount = 0
n = int(input())
A = list(map(int, input().split()))
mergeSort(0, n - 1)
print(swapCount)
