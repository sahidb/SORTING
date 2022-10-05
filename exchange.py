def exchange_sort(a):
    n = len(a)
    # outer loop
    for i in range(0,n-1):
        # inner loop
        for j in range(i+1,n):
            # swap
            if a[i]>a[j]:
                a[i],a[j] = a[j],a[i]
                yield a, [i], [j], list(range(0,i))


