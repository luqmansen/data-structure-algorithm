def generateStaircase(int_param):
  blank_space = int_param - 1
  for i in range(1,int_param+1,1):
    if blank_space < 0:
      break
    print(" "*blank_space, "#"*i)
    blank_space = blank_space - 1
  
generateStaircase(6)
