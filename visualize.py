import random
from matplotlib import pyplot

def visualize (sorting_alg, n):

    #create array
    a = random.sample(range(1,n+1), n)
    sorting_process = sorting_alg(a)
    while True:
        next_a, hl1, hl2, hl3 = next(sorting_process, (None, None, None, None))
        if next_a is None :
            break
        else:
            bars = pyplot.bar(x=range(1, len(a) + 1), height=next_a)
            for h in hl1:
                bars[h].set_color("red")
            for h in hl2:
                bars[h].set_color("orange")
            for h in hl3:
                bars[h].set_color("green")
            pyplot.axis("off")
            pyplot.pause(0.01)
            pyplot.clf()

    pyplot.show()