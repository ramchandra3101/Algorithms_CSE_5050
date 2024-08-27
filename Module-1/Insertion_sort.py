def insertion_sort(Arr, n):
  for j in range(n):
    key = Arr[j]
    i = j - 1
    while i >= 0 and Arr[i] > key:
      Arr[i + 1] = Arr[i]
      i -= 1
      print(Arr)
    Arr[i + 1] = key
    print(Arr)

if __name__ == '__main__':
  Arr = [5, 2, 4, 6, 1, 3]
  insertion_sort(Arr, len(Arr))
  
