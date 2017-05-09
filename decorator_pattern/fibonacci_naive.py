def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


known = {0: 0, 1: 1}


def fibonacci_improved(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci_improved(n-1) + fibonacci_improved(n-2)
    known[n] = res
    return res

if __name__ == '__main__':
    from timeit import Timer
    t = Timer()
    fibonacci_improved(50)
    print(t.timeit())
    print fibonacci_improved(50)