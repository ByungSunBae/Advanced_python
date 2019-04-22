## Naive grouper function with tuple and list

def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

for _ in naive_grouper(range(100000000), 10):
    pass

## In my computer,
## Used Memory : about 4.5GB
## User time (seconds) : about 7s
