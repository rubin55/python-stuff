#!/usr/bin/env python3

from functools import lru_cache
from sys import argv
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)


def fib5(i: int) -> int:
    if i == 0:
        return i
    l: int = 0
    n: int = 1
    for _ in range(1, i):
        l, n = n, l + n
        # yield n
    return n


if __name__ == '__main__':
    print(fib5(int(argv[1])))
