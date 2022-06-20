def all_construct(word: str, bank: list[str]) -> list[list[str]]:
    if word == "":
        return [[]]

    result = []
    for w in bank:
        prefix_removed = word.removeprefix(w)
        if len(prefix_removed) == 0:
            return [[w]]
        elif len(prefix_removed) < len(word):
            comb = all_construct(prefix_removed, bank)
            for i in comb:
                i = [w, *i]
                result.append(i)

    return result


if __name__ == "__main__":
    s = all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
    # s = all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    #                   ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])  # false
    print(s)
