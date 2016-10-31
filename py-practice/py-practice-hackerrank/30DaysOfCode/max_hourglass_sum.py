# CHALLENGE: https://www.hackerrank.com/challenges/30-2d-arrays

def build_arr():
    arr = []
    for arr_i in range(6):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    return arr

def is_square_arr(arr):
    for e in arr:
        if len(e) != len(arr):
            raise ValueError('Input is not a n * n 2d array')
    return True

def calc_hourglass_sums(arr):
    sums = []
    if is_square_arr(arr):
        n = len(arr)
        for i in range(0, n - 2):
            for j in range(0, n - 2):
                hourglass_sum = sum(arr[i][j:j+3]) + sum(arr[i+2][j:j+3]) + arr[i+1][j+1]
                sums.append(hourglass_sum)
        return sums


arr = build_arr()
sums = calc_hourglass_sums(arr)

print(max(sums))
