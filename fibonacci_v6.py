#!/usr/local/bin/python3


def fibonacci(quantit):
    result = [0, 1 ]
    while True:
        result.append(sum(result[-2:]))
        if len(result) == quantit:
            break
    return result


if __name__ == '__main__':
    # Listar os 20 primeiros npumeros da sequência
    for fib in fibonacci(20):
        print(fib)
