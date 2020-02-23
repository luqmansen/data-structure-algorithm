def populate_arr(arr):
    with open("input") as file:
        for i, str in enumerate(file):
            arr.append(str.rstrip())


input = []
populate_arr(input)


def separate_var(arr):
    ct = 0
    s, t, a, b = 0, 0, 0, 0
    for i in arr:
        if ct > 4:
            ct = 0
        else:
            if ct == 0:
                s, t = i.split(' ')
            elif ct == 1:
                a, b = i.split(' ')
            elif ct == 3:
                apple = []
                for val in i.split(' '):
                    apple.append(int(val))
            elif ct == 4:
                orange = []
                for val in i.split(' '):
                    orange.append(int(val))
            ct += 1
    return int(s), int(t), int(a), int(b), apple, orange


def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i, apl in enumerate(apples):
        apples[i] = apl+a

    for i, org in enumerate(oranges):
        oranges[i] = org+b

    apple_count = 0
    orange_count = 0
    for apl in apples:
        if s <= apl <= t:
            apple_count+=1
    for org in oranges:
        if s <= org <= t:
            orange_count+=1

    print(apple_count)
    print(orange_count)















