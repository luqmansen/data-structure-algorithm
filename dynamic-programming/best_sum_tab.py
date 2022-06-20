def how_sum(target: int, numbers: list[int]) -> list[int]:
    tab = [None] * (target + 1)
    tab[0] = []

    for i in range(target + 1):
        if tab[i] is not None:
            for _, n in enumerate(numbers):
                if i + n <= target:
                    new = [*tab[i], n]
                    if tab[i + n] is not None:
                        if len(new) < len(tab[i + n]):
                            tab[i + n] = new
                    else:
                        tab[i + n] = new
    # print(tab)
    return tab[target]


if __name__ == '__main__':
    print(how_sum(7, [7, 3, 4, 5, 2,1]))
