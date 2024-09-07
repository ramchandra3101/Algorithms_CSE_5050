def Compute_sum_array(arr):
  prefix_sum=[0]*(len(arr)+1)
  for k in range(1, len(arr)+1):
    prefix_sum[k] = prefix_sum[k-1] + arr[k-1]
  
  result =[[0] *len(arr) for _ in range(len(arr))]
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      result[i][j] = prefix_sum[j+1] - prefix_sum[i]
 
  return result
if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  print(Compute_sum_array(arr))
