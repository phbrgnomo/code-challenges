
# Initial Solution
# Get an integer input from the user, representing the number of test cases
i = int(input().strip())

# Iterate for each test case
for _ in range(i):
    # Get a string input for each test case
    s = input().strip()
    
    # Initialize two empty strings to store characters at even and odd indices
    string1 = ''
    string2 = ''
    
    # Iterate through the characters of the input string
    for ind in range(len(s)):
        # Check if the current index is even
        if ind % 2 == 0:
            # Concatenate the character at the even index to string1
            string1 = string1 + string1.join(s[ind])
        # Check if the current index is odd
        if ind % 2 == 1:
            # Concatenate the character at the odd index to string2
            string2 = string2 + string2.join(s[ind])
    
    # Print the concatenated strings for even and odd indices
    print(f"{string1} {string2}")

# Optimized Solution
# Get number of test cases
n = int(input().strip())

# Iterate for each test case
for _ in range(n):
    # Get a string input for each test case
    s = input()

    # Initialize empty strings for even and odd indices
    even = ""
    odd = ""

    # Iterate through the characters of the string along with their indices
    for i, char in enumerate(s):
        # Check if the current index is even
        if i % 2 == 0:
            # Concatenate the character at the even index to the even string
            even += char
        else:
            # Concatenate the character at the odd index to the odd string
            odd += char

    # Print the concatenated strings for even and odd indices
    print(even, odd)
