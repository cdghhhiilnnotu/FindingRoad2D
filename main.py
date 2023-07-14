import numpy as np
import random

main_arr_path = []
#   long(arr, x, y, i, b)
def long(arr, a, b, c, d):
    if min(a,c) != a:
        a,c = c, a
        b,d = d, b
    temp = 0
    for i in range(a, c+1):
        if b == 0:
                temp += arr[i][d]
        else:
                temp += arr[i][b]

    return temp
#   find(arr, n, m, i, b, b+1, demT, demN)
#   find(arr, n, m, i, 0, 1, 0, demN)
def find(arr, n, m, x, y, b, dem, demN, sub_arr):
    for i in range(0, n):
        new_sub_arr = sub_arr.copy()
        if arr[i][b] == 0:
            if long(arr, x, y, i, b) == 0:
                demT = dem + (abs(x-i) + 1)
                # print(demT)
                for l in range(min(x, i)+1, max(x, i)+1):
                    new_sub_arr.append([l,(b if x>i else y)])
                new_sub_arr.append([i,b])
                # print(new_sub_arr)
                if y != m-2:
                    demN = find(arr, n, m, i, b, b+1, demT, demN,new_sub_arr)
                else:
                    if demT < demN:
                        global main_arr_path
                        main_arr_path = new_sub_arr.copy()
                    demN = min(demN, demT)

    return demN

# arr=[[1,1,1,1,1,1],
#      [0,1,1,0,0,1],
#      [0,0,1,0,0,0],
#      [1,1,1,1,1,1],
#      [1,0,0,0,1,0],
#      [0,0,1,0,1,0]
#      ]
# n = 6
# m = 6
# arr =  [[0, 1, 0, 1, 1, 1, 1, 1],
#         [1, 1, 0, 1, 0, 0, 0, 1],
#         [1, 1, 1, 0, 0, 1, 0, 1],
#         [1, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0, 0]]
# n = 5
# m = 8
# --------
# [[0 1 0 1 1 1 1 1],
#  [1 1 0 1 0 0 0 1],
#  [1 1 1 0 0 1 0 1],
#  [1 0 0 0 0 1 0 0],
#  [0 0 0 0 1 1 0 0]] output 11 should 13
# --------
n = random.randint(3,10)
m = random.randint(3,10)
arr = np.random.rand(n, m)
arr = np.where(arr > 0.5, 1, 0)
print(arr)

demN = n*m
for i in range(0, n):
    if arr[i][0] == 0:
        arr1  = [[i,0]]
        demN = find(arr, n, m, i, 0, 1, 0, demN, arr1)
if demN != n*m:
    print(demN + 1)
else:
    print('Khong co duong')

# for i in main_arr_path:
#     print(i)
print(len(main_arr_path))
print(main_arr_path)




