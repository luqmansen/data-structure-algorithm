def how_sum(target: int, numbers: list[int]) -> list[int]:
    tab = [None] * (target + 1)
    tab[0] = []

    # 7 [3,4,5]
    #   0   1      2    3       4       5      6      7
    # [[], None, None, [[3]], [[4]], [[5]], [[3]], [[4]]]
    for i in range(target + 1):
        if tab[i] is not None:
            for _, n in enumerate(numbers):
                if i + n <= target:
                        tab[i + n] = [*tab[i], n]
    # print(tab)
    return tab[target]


if __name__ == '__main__':
    print(how_sum(7, [3, 4, 5, 7, 2]))
