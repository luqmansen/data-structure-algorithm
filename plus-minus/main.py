

def countNumbers(array_param):
  positives, negatives, zeros = 0,0,0
  for number in array_param:
    if number > 0:
      positives = positives + 1
    elif number < 0:
      negatives = negatives + 1
    else:
      zeros = zeros + 1
  # print(positives, negatives, zeros)
  if positives + negatives + zeros == len(array_param):
    pos_fragment = positives / len(array_param)
    neg_fragment = negatives / len(array_param)
    zero_fragment = zeros / len(array_param)
    return pos_fragment, neg_fragment, zero_fragment
  else:
    return "Error: length is not equal"

print(countNumbers([-4,3,-9,0,4,1]))
