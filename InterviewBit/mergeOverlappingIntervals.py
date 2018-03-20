def mergeOverlappingIntervals(a):
    a.sort(key=lambda x: x[0])

    na = [a[0]]
    index = 0

    for i in range(1, len(a)):

        if na[index-1][1] > a[i][0]:

            while index != 0 and na[index-1][1] > a[i][0]:
                na[index-1][0] = min(na[index-1][0], a[i][0])
                na[index-1][1] = max(na[index-1][1], a[i][1])
                index -= 1

        else:
            na.append(a[i])

        index += 1

    return na

arr = [[1,3],[2,6],[8,10],[15,18]]
print(mergeOverlappingIntervals(arr))