## This is better function than in naive.py because of using iterator.

def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

for _ in better_grouper(range(100000000), 10):
    pass
## 1) without the reference to the len() built-in, better_grouper() can
## take any iterable as an argument (even infinite iterators).
## 2) by returning an iterator rather than a list, better_grouper() can
## process enormous iterables without trouble and uses much less memory.

## In my computer,
## Used Memory : about 6308KB
## User time (seconds) : about 1.4s
