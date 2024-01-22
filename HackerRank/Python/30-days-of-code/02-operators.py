#!/bin/python3

# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    """
    Calculate the total cost of a meal including tip and tax.

    Args:
        meal_cost (float): The cost of the meal.
        tip_percent (int): The percentage of the meal cost to be added as tip.
        tax_percent (int): The percentage of the meal cost to be added as tax.

    Returns:
        None

    Explanation:
        This function calculates the tip and tax amounts based on the meal cost and 
        the provided tip and tax percentages.
        It then adds the tip and tax amounts to the meal cost and prints the rounded 
        total cost.
    """
    # Write your code here

    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    print(round(meal_cost + tip + tax))
    
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
