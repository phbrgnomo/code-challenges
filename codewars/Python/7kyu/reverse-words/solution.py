
"""
Initial solution:

def reverse_words(text: str) -> str:
    # Split the input text into a list of words using space as the delimiter
    words = text.split(' ')

    # Initialize an empty string to store the reversed words
    new_text = ''

    # Iterate over each word in the list
    for _ in words:
        # Reverse the characters in the word and join them back together
        r_word = ''.join(reversed(_))

        # Append the reversed word to the new_text string with a space after it
        new_text += f'{r_word} '

    # Remove any trailing whitespace from the new_text string and return it
    return new_text.rstrip()
"""

"""
Improved solution:
- The list comprehension word[::-1] for word in text.split(' ') reverses each word in 
the split text list.
- The join method is used to concatenate the reversed words with spaces, which also 
avoids the need to strip trailing whitespace.

"""
def reverse_words(text: str) -> str:
    return ' '.join(word[::-1] for word in text.split(' '))
