"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

"""

# Check if the script is being run as the main program
if __name__ == '__main__':
    
    # Get user input for the variable 'n' and convert it to an integer
    n = int(input().strip())

    # Check if 'n' is odd or falls within the range [6, 20]
    if n % 2 == 1 or (n >= 6 and n <= 20):
        print("Weird")
    # Check if 'n' is even and falls within the range [2, 5] or is greater than 20
    elif 2 <= n <= 5 or n > 20:
        print("Not Weird")

