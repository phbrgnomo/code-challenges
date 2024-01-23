def leap_year(year):
    """
    Checks if a given year is a leap year.

    This function takes a year as input and checks if it is a leap year. A leap year 
    is defined as a year that is divisible by 4 and not divisible by 100, or a year 
    that is divisible by 400.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """

    # Check if the year is divisible by 4 and not divisible by 100, or if it is divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0