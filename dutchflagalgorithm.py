
a = [0,1,2,0,2,1,2,0,1,1,1,2,2,2,1,1,1,1,0,1,1,2,0,1,0,1]


i = 0
j = 0
k = len(a) - 1
mid = 1

while j <= k:
    if a[j] < mid:
        q = a[j]
        a[j] = a[i]
        a[i] = q
        i = i + 1
        j = j + 1
    elif a[j] > mid:
        q = a[k]
        a[k] = a[j]
        a[j] = q
        k = k-1
    else:
       j = j + 1

print(a)





