def getTotal(arr: list, brr: list):
    considered = []
    for i in range(1, 101):
        for j in arr:
            if i % j == 0:
                considered.append(i)

    considered_two = []
    for i in considered:
        for j in brr:
            if i % j == 0:
                considered_two.append(j)

    return len(set(considered_two))


# print(getTotal([2, 4], [16, 32, 96]))
# getTotal([3, 4], [24, 48])
# print(getTotal([2], [20, 30, 12]))
# getTotal([3, 9, 6], [36, 72])
print(getTotal([100, 99, 98, 97, 96, 95, 94, 93, 92, 91],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
