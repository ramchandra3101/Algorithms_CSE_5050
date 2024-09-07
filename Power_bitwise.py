def powerbitwise(x,y):
  result=1
  while y:
    if y & 1 == 1:
      result = result * x
    x*=x
    y=y>>1
  return result

if __name__ == '__main__':
  x = 2
  y = 7
  print(powerbitwise(x,y))
