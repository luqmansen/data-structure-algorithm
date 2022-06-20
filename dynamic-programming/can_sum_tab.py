

def can_sum(target: int, numbers: list[int]):
    tab = [False] * (target + 1)
    tab[0] = True
    for i in range(target+1):
        if tab[i] is True:
            for num in numbers:
                if i+num <= target:
                    tab[i+num] = True

    return tab[target]


if __name__ == '__main__':
    print(can_sum(7,[2,3]))
    print(can_sum(7,[2,4]))
    print(can_sum(7,[2,5,8]))
    print(can_sum(5,[3,4,7]))