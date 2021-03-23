import math
from time import perf_counter
from numba import njit


@njit(fastmath=True)
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


@njit(fastmath=True)
def main(N):
    for i in range(N):
        is_prime(i)


if __name__ == '__main__':
    N = 10000000
    start = perf_counter()
    main(N)
    end = perf_counter()
    print(end - start)
