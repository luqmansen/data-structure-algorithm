import math


def binary_search(arr: list, target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return -1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(arr, 8))
