def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b

def ips(arr, a, b, c, d, m):
    if min(a,c) != a:
        a,c = swap(a, c)
        b,d = swap(b, d)
    temp = 0
    if b == 0:
        for i in range(a, c+1):
            temp += arr[i][d]
    elif b == m-2:
        for i in range(a, c+1):
            temp += arr[i][b]
    else:
        for i in range(a, c+1):
            temp +=  arr[i][d]
        if temp != 0:
            temp = 0
            for i in range(a, c+1):
                temp += arr[i][b]
    
    return temp

def long(arr, a, b, c, d, m):
    if min(a,c) != a:
        a,c = swap(a, c)
        b,d = swap(b, d)
    
    return abs(a-c) + 1

arr=[[0,1,0],
     [1,0,0],
     [1,0,0],
     [0,0,0],
     [1,0,0],
     [0,0,0]
     ]
n = 6
m = 3
print('||', end='')
for j in range(0, m):
    print(f'{j}-',end='')
print()
for i in range(0, n):
    print(f'{i}|', end='')
    for j in range(0,m):
        print(f'{arr[i][j]} ', end='')
    print()
for i in range(0, n):
    print(f'A[0][0] --> A[{i}][1] = ', end='')
    print(f'{ips(arr, 0, 0, i, 1, m)} ', end='')
    if ips(arr, 0,0,i, 1, m)  == 0:
        print(long(arr, 0, 0, i, 1, m), end='')
    print()
print('-------------------------------------------')
for i in range(0, n):
    print(f'A[3][0] --> A[{i}][1] = ', end='')
    print(f'{ips(arr, 3, 0, i, 1, m)} ', end='')
    if ips(arr, 3, 0, i, 1, m)  == 0:
        print(long(arr, 3, 0, i, 1, m), end='')
    print()
print('-------------------------------------------')
for i in range(0, n):
    print(f'A[5][0] --> A[{i}][1] = ', end='')
    print(f'{ips(arr, 5, 0, i, 1, m)} ', end='')
    if ips(arr, 5, 0,i, 1, m)  == 0:
        print(long(arr, 5, 0, i, 1, m), end='')
    print()
print('-------------------------------------------')

