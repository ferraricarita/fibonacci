#!/usr/local/bin/python3


def fibonacci(limit):
    penult = 0
    last = 1
    print(f'{penult}, {last}', end=',')
    while last < limit:
        next = penult + last
        print(next, end=',')
        penult = last
        last = next


if __name__ == '__main__':
    fibonacci(10000)
