def maxSubarraySum(arr):


 # Stores the result (maximum sum found so far)
 res = arr[0]


 # Maximum sum of subarray ending at current position
 maxEnding = arr[0]


 for i in range(1, len(arr)):


   # Either extend the previous subarray or start
   # new from current element
   maxEnding = max(maxEnding + arr[i], arr[i])


   # Update result if the new subarray sum is larger
   res = max(res, maxEnding)


 return res


if __name__ == "__main__":
 arr = [2, 3, -8, 7, -1, 2, 3]
 print(maxSubarraySum(arr))
