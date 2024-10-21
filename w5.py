A = [10, 5, 1, 6, 9, 2, 6, 9, 10, 8]
B = [13, 9, 1, 8, 10, 7, 3, 4, 18, 2]
C = [86, 10, 26, 66, 97, 35, 69, 31, 89, 67]

################################


def find_median(arr):
    arr.sort()
    # n = len(arr)
    # if n % 2 == 0:
    #     return (arr[n // 2 - 1] + arr[n // 2]) / 2
    # else:
    #     return arr[n // 2]
    return arr[len(arr) // 2]


def find_max(arr):
    return max(arr)


def find_min(arr):
    return min(arr)


def get_standard_deviation_of_median(arr, median):
    variance_of_median = sum((x - median) ** 2 for x in arr) / (len(arr)-1)

    return variance_of_median ** 0.5


min_A, max_A = find_min(A), find_max(A)
median_A = find_median(A)

min_B, max_B = find_min(B), find_max(B)
median_B = find_median(B)

min_C, max_C = find_min(C), find_max(C)
median_C = find_median(C)

################################

print(max_A, min_A, median_A)
print(max_B, min_B, median_B)
print(max_C, min_C, median_C)

################################

sdm_A = get_standard_deviation_of_median(A, median_A)
sdm_B = get_standard_deviation_of_median(B, median_B)
sdm_C = get_standard_deviation_of_median(C, median_C)

################################

print(sdm_A)
print(sdm_B)
print(sdm_C)
