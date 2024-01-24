def reverse(text):
    """
    [::-1]: This is known as slicing in Python. The syntax start:stop:step is used for 
    slicing, and when any of these parameters is omitted, it takes on its default value.
    In this case, [::-1] means the entire string (start and stop are omitted), but with 
    a step of -1.

    start: Default is the beginning of the sequence.
    stop: Default is the end of the sequence.
    step: Negative step value indicates a reversed seq
    """
    return text[::-1]

print(reverse("I'm hungry!"))