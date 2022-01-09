def fib(n):
    if n < 1:
        return
    if n < 3:
        return 1
    
    e1 = e2 = 1
    the_sum = 0
    for i in range(3, n+1):
        the_sum = e1 + e2
        e1, e2 = e2, the_sum
    return the_sum
    
for n in range(1, 10):
    print(n, "->", fib(n))