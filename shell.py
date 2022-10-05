import math


def shell_gaps(n):
    g, gaps = n // 2, []
    while g > 0:
        gaps.append(g)
        g = g // 2
    return gaps

def hibbard_gaps(n):
    i, g, gaps = 0, 0, []
    while g < n:
        i+=1
        g = 2 ** i - 1
        gaps.append(g)
    gaps.reverse()
    return gaps

def papernov_stasevich_gaps(n):
    i, g, gaps = 0, 0, [1]
    while g < n:
        i += 1
        g = 2 ** i + 1
        gaps.append(g)
    gaps.reverse()
    return gaps

def knuth_gaps(n):
    i,g,gaps = 0,0,[]
    while g < n:
        i+=1
        g=(3**i-1)//2
        gaps.append(g)
    gaps.reverse()
    return gaps

def tokuda_gaps(n):
    i,g,gaps = 0,0,[]
    while g < n:
        i+=1
        g=math.ceil(1/5*(9*(9/4)**(i-1)-4))
        gaps.append(g)
    gaps.reverse()
    return gaps

def sedgewick_gaps(n):
    i,g,gaps = 0,0,[1]
    while g < n:
        i+=1
        g=4**i+3*2**(i-1)+1
        gaps.append(g)
    gaps.reverse()
    return gaps

def ciura_gaps(n):
    return[11750,701, 301, 132, 57, 23, 10, 4, 1]

gaps_dict={
    "shell" : shell_gaps,
    "hibbard" : hibbard_gaps,
    "papernov" : papernov_stasevich_gaps,
    "knuth" : knuth_gaps,
    "tokuda" : tokuda_gaps,
    "sedgewick" : sedgewick_gaps,
    "ciura" : ciura_gaps
}

def shell_sort(a, sequence = "shell"):
    n = len(a)
    # gaps = shell_gaps(n)
    gaps = gaps_dict.get(sequence)(n)
    for gap in gaps:

        # outer loop go forward
        for i in range(gap, n):
            # store current element
            current_element = a[i]
            # inner loop go backward
            j = i
            while current_element < a[j-gap] and j>=gap:
                yield a, [i], [j-gap], []
                # copy over element(from left to right)
                a[j] = a[j-gap]
                # step left
                j-=gap
            # insert the stored array element
            a[j] = current_element
            # yield  a, [], [j], [i]


    

