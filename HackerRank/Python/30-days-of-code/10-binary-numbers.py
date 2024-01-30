#!/bin/python3


# Check if the script is being run as the main program
if __name__ == '__main__':
    # Take an integer input from the user and remove leading/trailing whitespaces
    n = int(input().strip())
    
    # Convert the integer to binary representation and remove the '0b' prefix
    b = bin(n)[2:]

    # Find the maximum sequence of consecutive 1s by splitting the binary string at 0s and taking the maximum part
    maxseq = max(b.split('0'))

    # Print the length of the maximum sequence of consecutive 1s
    print(len(maxseq))
