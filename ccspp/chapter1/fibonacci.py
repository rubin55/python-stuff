#!/usr/bin/env python3

from sys import argv


def fib1(n: int) -> int:
    print('fib1({0})'.format(n))
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    print('fib2({0})'.format(n))
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    print(fib2(int(argv[1])))
