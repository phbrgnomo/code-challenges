#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    # n = 4
    arr = list(map(int, input().rstrip().split()))
    # arr = [1, 4, 3, 2]

    while n > 0:
        print(f"{arr[n-1]} ", end='')
        n -= 1