"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    lnum = [number, number + 1, number + 2]
    return lnum

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    clist = rounds_1 + rounds_2
    return clist


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    for n in rounds:
        if n == number:
            return True
    
    return False

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    s = 0
    for c in hand:
        s += c
    q = len(hand)
    return s / q


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    avrfl = (hand[0] + hand[-1]) / 2
    midcard = hand[len(hand) // 2]
    return avrfl == card_average(hand) or midcard == card_average(hand)

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    if len(hand) == 0:
        return True  # If the list is empty, consider it equal
    
    even_sum = sum(hand[i] for i in range(0, len(hand), 2))
    odd_sum = sum(hand[i] for i in range(1, len(hand), 2))

    # Calculate the number of even and odd indexed elements
    even_count = (len(hand) + 1) // 2
    odd_count = len(hand) // 2

    return (even_sum / even_count) == (odd_sum / odd_count) if odd_count > 0 else True


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    return hand