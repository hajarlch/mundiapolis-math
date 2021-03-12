def add_arrays(arr1, arr2):
    m = len(arr1)
    result = []
    if (len(arr1) == len(arr2)):
        for x in range(m):
            result.append(arr1[x] + arr2[x])
        return result
    return None
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))
