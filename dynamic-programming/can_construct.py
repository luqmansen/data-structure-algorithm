"""
worst case: ever string in word bank is prefix of the target
eg: eeeeeeeef, [e,eee,eeeee,eeeeee,eeeeeee]
m = word length
n = word bank length

bruteforce
time:  O(n^m * m) where last m is from remove prefix function
space O(m*m) where first m is from the deepest stack, and second m is from creating new string

memoization
time:
"""


def can_construct(word: str, word_bank: list[str], memo=None) -> bool:
    if memo is None:
        memo = {}
    if word in memo:
        return memo[word]
    if word == "":
        return True

    for w in word_bank:
        # if w is either prefix of word, else, skip it
        prefix_removed = word.removeprefix(w)  # this operation space and time complexity is O(n)
        if len(prefix_removed) == 0:
            memo[word] = True
            return True
        if len(prefix_removed) < len(word):
            # print("prefix_removed:", prefix_removed)
            if can_construct(prefix_removed, word_bank, memo):
                memo[word] = True
                return True

    memo[word] = False
    return False


if __name__ == "__main__":
    # s = can_construct("abcdef", ["ab", "bc", "cde", "f"])  # true
    s = can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"])  # false
    print(s)
