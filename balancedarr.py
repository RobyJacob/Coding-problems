def balancedSum(arr):
    # Write your code here
    acc_sum = [0 for j in range(len(arr)+1)]

    for j in range(len(arr)):
        acc_sum[j+1] = arr[j] + acc_sum[j]

    total = sum(arr)

    for i in range(len(arr)):
        left_arr_sum = acc_sum[i]
        right_arr_sum = total - acc_sum[i+1]
        if left_arr_sum == right_arr_sum:
            return i

print(balancedSum([1, 2, 3, 3]))
