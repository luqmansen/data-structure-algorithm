import numpy as np
import matplotlib.pyplot as plt


# linspace -> start, stop, sample generated (evenly)
# x = np.linspace(0, 10, 30)
# y = np.sin(x)

# Sorting

def bubbleSort(arr):
    n = len(arr)
    ret_arr = []
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break
    for i in range(len(arr)):
        ret_arr.append(arr[i])
    return ret_arr


# Length Equality Checker
def isEqualLen(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    else:
        return True

# plt.plot(x,y, '-ok')

# Calculating Linear Regression using Least Square

# y = b0 + b1 * x

"""
   Menentukan nilai b1 dan b2 
   1.) Tentukan mean x dan mean y, dapat nilai awal (y = mean y dan x = mean x)
   2.) Lalu tiap nilai (x - mean x) dan (tiap nilai y) - (mean y),
   3.) Lalu kuadrat dari (tiap nilai x) - (mean x),
   4.) Lalu hasil kali dari dua elemen di 3.)
   5.) b1 adalah jumlah dari 3.) dibagi dengan jumlah dari 4.)
   6.) b0 adalah y - b1 * x, dengan y = mean y dan x = mean x
"""


def sum(sum_param):  # expecting ndarray/list as input
    sum_val = 0
    for val in sum_param:
        sum_val = sum_val + val
    return sum_val


def mean(mean_param):  # expecting ndarray/list as input
    mean_val = 0
    for val in mean_param:
        mean_val = mean_val + val
    mean_val = mean_val / len(mean_param)
    return mean_val


def diff_to_mean(step_param):  # 'Varian individual' dalam standar deviasi
    diffed_vals = ([])
    mean_val = mean(step_param)
    for val in step_param:
        diffed_vals.append(val - mean_val)
    return diffed_vals


def square_diff(step_param):  # expecting ndarray/list as input
    squared_vals = ([])
    square_val = diff_to_mean(step_param)
    for val in square_val:
        squared_vals.append(val ** 2)
    return squared_vals


def calc_stdDev(varian_param, return_variance=False):  # expecting ndarray/list as input
    temp_sum = sum(square_diff(varian_param))
    variance = temp_sum / len(varian_param)
    stdDev = np.sqrt(variance)
    if return_variance == True:
        return variance
    else:
        return stdDev


def calc_bCoefs(x_coords, y_coords):
    pembilang = ([])
    penyebut = square_diff(x_coords)
    if not isEqualLen(x_coords, y_coords):
        print("Index Length mismatch!")
        return
    else:
        for i in range(len(x_coords)):
            pembilang.append(diff_to_mean(x_coords)[i] * diff_to_mean(y_coords)[i])
    b1 = sum(pembilang) / sum(penyebut)
    b0 = mean(y_coords) - b1 * mean(x_coords)
    coefs = ([b0, b1])
    return coefs


def calc_est_coords(x_coords, y_coords, return_y_accs=False):
    b = calc_bCoefs(x_coords, y_coords)
    y_acc = None
    est_coords = ([
        [],  # X Axis Coordinates
        []  # Y Axis Coordiantes
    ])
    for i in range(len(x_coords)):
        est_coords[0].append(x_coords[i])
        y_acc = b[1] * x_coords[i]  # y_accent = b0 + (b1 * x)
        y_acc = y_acc + b[0]  # idk how math operation works in Py
        est_coords[1].append(round(y_acc, 2))
    if return_y_accs:
        return est_coords[1]
    else:
        return est_coords


def rSquare(x_coords, y_coords):
    actual_dist = sum(square_diff(y_coords))  # jumlah dari (y - mean_y) ^ 2
    est_vals = ([])
    for y_accs in calc_est_coords(x_coords, y_coords, return_y_accs=True):
        temp_val = y_accs - mean(y_coords)
        temp_val = temp_val ** 2
        est_vals.append(temp_val)
    est_dist = sum(est_vals)  # jumlah dari (y_accent - mean_y) ^ 2
    rsquare = est_dist / actual_dist
    return round(rsquare, 2)


# Standard Error of the Estimate
def meanSquare(x_coords, y_coords):
    error, index = 0, 0
    pembilang = ([])
    for y_acc in calc_est_coords(x_coords, y_coords, return_y_accs=True):
        temp_val = y_acc - y_coords[index]
        temp_val = temp_val ** 2
        pembilang.append(round(temp_val, 2))
        index = index + 1
    pembilang = sum(pembilang)
    penyebut = len(x_coords) - 2
    error = np.sqrt(pembilang / penyebut)
    return round(error, 2)
    
# print(calc_stdDev([4,4,4,4,4,4,4,4,4], True))
