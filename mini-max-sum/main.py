from stat_funcs import *

def generateSum(list_param):
  init_num_list = list_param
  init_sum = []
  for i in init_num_list:
    init_sum.append(sum(init_num_list)-i)
  init_sum = bubbleSort(init_sum)
  return init_sum[0], init_sum[len(init_sum) - 1]

print(generateSum([1,2,3,4,5]))
