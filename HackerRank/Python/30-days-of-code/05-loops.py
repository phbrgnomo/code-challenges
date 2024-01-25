#!/bin/python3

if __name__ == '__main__':
    # Get an integer input from the user
    n = int(input().strip())
    
    # Iterate from 1 to 10 (inclusive)
    for i in range(10):
        # Print the multiplication table entry for the current iteration
        print(f"{n} x {i+1} = {n * (i+1)}")
