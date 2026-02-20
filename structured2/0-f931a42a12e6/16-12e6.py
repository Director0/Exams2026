import threading
from sys import setrecursionlimit


def f(n):
    if n <= 1000:
        return n ** (n ** 2)
    else:
        return n + 2 * f(n - 2) + 6 * f(n - 6)




if __name__ == "__main__":
    setrecursionlimit(1000000000)
    threading.stack_size(200000000)
    thr = threading.Thread(target=f(20024) - 2 * f(20022) - 3 * f(20020) + 18 * f(20014))
    thr.start()
    print(f(20024) - 2 * f(20022) - 3 * f(20020) + 18 * f(20014))