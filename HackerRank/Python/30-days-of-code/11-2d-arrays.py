#!/bin/python3

""" First implementation
def hourglass_sum(line_1, line_2, line_3):
    return sum(line_1) + line_2 + sum(line_3)


if __name__ == '__main__':

    # test input
    # arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Initialize variables for the starting and ending lines of the hourglass
    start_line = 0
    end_line = 2

    # Initialize the maximum hourglass sum to negative infinity
    max_hs_value = float('-inf')

    # Iterate through possible hourglasses vertically
    for _ in range(4):
        # Extract the current lines forming the hourglass
        current_lines = arr[start_line:end_line+1]

        # Initialize the column index
        col = 0
        
        # Iterate through possible hourglasses horizontally
        for n in range(6):
            # Break if the last valid column index is reached
            if col == 3:
                break

            # Calculate the sum of the current hourglass
            hs = hourglass_sum(current_lines[0][col:col+3], current_lines[1][col+1], current_lines[2][col:col+3])

            # Update the maximum hourglass sum
            max_hs_value = max(max_hs_value, hs)

            # Move to the next column
            col += 1

        # Remove the first line to slide to the next set of hourglasses
        arr.pop(0)

    # Print the final maximum hourglass sum
    print(max_hs_value)
"""

# Simplified implementation
if __name__ == '__main__':

    # test input
    # arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Initialize the maximum hourglass sum to negative infinity
    max_hs_value = float('-inf')

    # Iterate through possible hourglasses
    for i in range(4):
        for j in range(4):
            # Calculate the sum of the current hourglass
            hs = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])

            # Update the maximum hourglass sum
            max_hs_value = max(max_hs_value, hs)

    # Print the result
    print(max_hs_value)