def insertion_sort(a):
    n = len(a)

    # outer loop go forward
    for i in range(1, n):
        # store current element
        current_element = a[i]
        # inner loop go backward
        j = i
        while current_element < a[j-1] and j>=1:
            yield a, [i], [j], []
            # copy over element(from left to right)
            a[j] = a[j-1]
            # step left
            j-=1
        # insert the stored array element
        a[j] = current_element
        yield  a, [], [j], [i]

