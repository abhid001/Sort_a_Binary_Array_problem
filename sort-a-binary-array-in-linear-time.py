'''
Input : 1 0 0 1 0 1 0 1 1 1 1 1 1 0 0 1 1 0 1 0 0 
Output : 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1
Explanation: The output is a sorted array of 0 and 1

Input : 1 0 1 0 1 0 1 0 
Output : 0 0 0 0 1 1 1 1
Explanation: The output is a sorted array of 0 and 1

Analysis:
  Problem Solved Successfully

  Total Time Taken: 4.01
  Accuracy: 100%

'''

def sort_binary_array_2(arr):
    i = 0
    j = 0
    n = len(arr)
    print(f'array length is {n}')
    for i in range(n):
        if arr[i] == 0:
            arr[j] = arr[i]
            j = j + 1

    for x in range(j, n):
        arr[x] = 1
        
    return arr
