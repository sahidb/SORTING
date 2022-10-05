def sift_down(a, start, end):
    root = start
    while True:
        #store the children and initialize swap
        left_child = 2 * root + 1
        right_child = left_child + 1
        swap = root

        # update swap if the left child exist and is greater than root
        if left_child <= end and a[left_child] > a[swap]:
            swap = left_child

        # update swap if the left child exist and is greater than root
        if right_child <= end and a[right_child] > a[swap]:
            swap = right_child

        if swap != root:
            yield a, list(range(start,end+1)), [swap], [root]
            a[root],a[swap]=a[swap],a[root]
            root = swap
        else:
            return


def heapify(a, n):
    start = (n-1) // 2
    end = n-1

    while start >= 0:
        yield from sift_down(a, start, end)
        start -= 1


def heap_sort(a):
    n = len(a)
    # building heap structure
    yield from heapify(a, n)

    # run selection sort on the heap
    end = n-1
    while end > 0:
        # swap first and last element
        a[end], a[0] = a[0], a[end]
        end -=1
        yield from sift_down(a,0, end)

