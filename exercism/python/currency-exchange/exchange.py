def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount / denomination)


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    num_bills = get_number_of_bills(amount, denomination)
    value = get_value_of_bills(denomination, num_bills)
    return float(amount - value)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_rate = float(spread / 100)
    print(spread_rate) # float spread rate
    real_rate = exchange_rate * (1 + spread_rate) # real extchange rate
    print(real_rate)
    max_new_money = exchange_money(budget, real_rate) # max amount of new money
    print(max_new_money)
    amnt_bills = get_number_of_bills(max_new_money, denomination) # get possible amount of bills
    print(amnt_bills)
    return get_value_of_bills(denomination, amnt_bills) # return que total value of the exchanged new money