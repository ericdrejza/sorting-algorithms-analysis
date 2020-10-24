# Python Heapsort Implementation

from math import inf

def insert(a, v):
    a.append(v)
    upheap(a, len(a)-1)

def upheap(a, k):
    v  = a[k]
    a[0] = int(10^10)
    while (a[int(k/2)] <= v and k > 1):
        a[k] = a[int(k/2)]
        k = int(k/2)
    a[k] = v

def remove(a):
    N = len(a)-1
    if N > 0:
        v = a[1]
        a[1] = a[N]
        dk = a.pop()
        downheap(a, N-1, 1)
        return v
    else:
        return 0

def downheap(a, N, k):
    if N > 0:
        v = a[k]
        while k <= (N/2):
            j = k + k
            if (j < N and a[j] < a[j+1]):
                j = j + 1
            if v >= a[j]:
                break
            a[k] = a[j]
            k = j
        a[k] = v

def heapsort(a):
    b = [0]
    for i in range(0, len(a)):
        insert(b, a[i])

    N = len(b) - 1
    
    while N > 0:
        a[N-1] = remove(b)
        N = N - 1