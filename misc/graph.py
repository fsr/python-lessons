from itertools import groupby, chain
from functools import partial


uncurry = lambda func: lambda args: func(*args)
flip = lambda func: lambda a, b: func(b, a)


graph = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('B', 'E'),
    ('D', 'G'),
    ('D', 'H'),
    ('D', 'F'),
    ('E', 'H'),
    ('G', 'I')
]


connectionmap = dict(
    map(uncurry(lambda a, b: (a, list(b))), chain(
        groupby(graph, partial(flip(tuple.__getitem__), 1)),
        groupby(graph, partial(flip(tuple.__getitem__), 0))
    ))
)

print(connectionmap)
