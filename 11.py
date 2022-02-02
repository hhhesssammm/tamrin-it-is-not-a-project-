def fib(n):
    i=0
    j=1
    yield i
    for x in range(n):
        yield j
        i, j = j, i + j

#example
print(list(fib(5)))
