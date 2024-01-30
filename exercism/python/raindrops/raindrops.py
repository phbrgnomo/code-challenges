def convert(number):
    # Initialize an empty string to store the response
    response = ''

    # Check if the number is divisible by 3, and add "Pling" to the response if true
    if int(number) % 3 == 0:
        response += "Pling"

    # Check if the number is divisible by 5, and add "Plang" to the response if true
    if int(number) % 5 == 0:
        response += "Plang"

    # Check if the number is divisible by 7, and add "Plong" to the response if true
    if int(number) % 7 == 0:
        response += "Plong"

    # If the response is still empty, the number is not divisible by 3, 5, or 7
    # Set the response to the string representation of the original number
    if not response:
        response = str(number)
    
    # Return the final response
    return response
