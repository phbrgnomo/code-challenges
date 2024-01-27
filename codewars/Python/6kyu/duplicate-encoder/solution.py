def duplicate_encode(word):
    # Create a dictionary to count the occurrences of each letter
    letter_counter = {}

    # Convert the word to lowercase to ensure case-insensitive comparison
    word = word.lower()

    # Iterate through each letter in the word
    for l in word:
        # Count the occurrences of each letter
        if letter_counter.get(l) is not None:
            counter = letter_counter.get(l)
            letter_counter[l] = (counter + 1)
        else:
            letter_counter[l] = 1
    # Return the result string based on the letter occurrences
    return ''.join('(' if letter_counter.get(l) == 1 else ')' for l in word)
