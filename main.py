# DEMO file

#   long(arr, x, y, i, b, m)
def long(arr, a, b, c, d, m):
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
def find(arr, n, m, x, y, b, dem, demN):
    for i in range(0, n):
        if arr[i][b] == 0:
            if long(arr, x, y, i, b, m) == 0:
                demT = dem + (abs(x-i) + 1)
                if y != m-2:
                    demN = find(arr, n, m, i, b, b+1, demT, demN)
                else:
                    demN = min(demN, demT)

    return demN

arr=[[0,0,0,1,0,0],
     [0,0,1,0,0,0],
     [0,0,1,0,1,0],
     [1,0,1,0,1,0],
     [1,0,0,0,0,0],
     [0,0,1,0,1,0]
     ]
n = 6
m = 6

demN = n*m
for i in range(0, n):
    if arr[i][0] == 0:
        demN = find(arr, n, m, i, 0, 1, 0, demN)
if demN != n*m:
    print(demN + 1)
else:
    print('Khong co duong')



