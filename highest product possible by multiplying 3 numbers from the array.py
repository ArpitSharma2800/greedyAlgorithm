def product(arr):
    n = len(arr)
    if n < 3:
        return -1
    arr.sort()
    return max(arr[0] * arr[1] * arr[n - 1],
               arr[n - 1] * arr[n - 2] * arr[n - 3])


A = [0, -1, 3, 100, -70, -50]
print(product(A))

