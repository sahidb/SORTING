import random

def bogo_sort(a):
    n = len(a)
    is_sorted = False
    while not is_sorted:
        #swaping 2 elements
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        a[i],a[j] = a[j],a[i]
        yield a, [i], [j], []
        #check if sorted
        is_sorted = True
        for i in range(1,n):
            if a[i]<a[i-1]:
                is_sorted = False
                break
