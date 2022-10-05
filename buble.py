def buble_sort(a):
    n = len(a)

    # outer loop
    for i in range(0,n):
        #inner loop
        for j in range(0, n-i-1):
            #make swap if necessary
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                yield a, [j+1],[],list(range(n-i,n))
