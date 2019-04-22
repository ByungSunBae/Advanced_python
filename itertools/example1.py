# From : https://realpython.com/python-itertools/
import itertools as itts

## Consider the built-in zip() function
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))

x = [1, 2, 3, 4]
x.__iter__()
x.__getitem__

## iter() built-in function
iter(x)

## map() built-in function
list(map(len, ['abc', 'de', 'fghi']))

## zip() and map()
list(map(sum, zip([1, 2, 3], [4, 5, 6])))


