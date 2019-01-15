#!/usr/local/bin/python3
def fibonacci(quantit, seq=(0, 1)):
    return seq if len(seq) == quantit else \
    fibonacci(quantit, seq + (sum(seq[-2:]),))


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
