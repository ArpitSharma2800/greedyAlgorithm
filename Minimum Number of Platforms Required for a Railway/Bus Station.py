def tracks(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    platform = 1
    result = 1
    i = 1
    j = 0
    while i < n and j < n:
        if(arr1[i] <= arr2[j]):
            platform = platform + 1
            i = i + 1
        elif(arr1[i] > arr2[j]):
            platform = platform-1
            j = j+1
        if(platform > result):
            result = platform
    print(result)


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
tracks(arr, dep, 6)
