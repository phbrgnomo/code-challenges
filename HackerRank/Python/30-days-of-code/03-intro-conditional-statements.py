#!/bin/python3


if __name__ == '__main__':
    N = int(input().strip())

    # Check if 'N' is odd or falls within the range [6, 20]
    if N % 2 == 1 or 6 <= N <= 20:
        print("Weird")
    # Check if 'N' is even and falls within the range [2, 5] or is greater than 20
    elif 2 <= N <= 5 or N > 20:
        print("Not Weird")
