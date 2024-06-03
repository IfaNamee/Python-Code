"""
Program: Lab8
Author: Ifa Namee
Date: 11/12/2023
purpose: This program is calculate total amount of books and average.
         using mipo method and import pyinputplus as pyip
"""

import pyinputplus as pyip

# Prices for different sandwich components.
prices = {
    'wheat': 4.0,
    'white': 3.50,
    'sourdough': 2.50,
    'chicken': 6.0,
    'turkey': 5.0,
    'ham': 4.5,
    'tofu': 4.0,
    'cheddar': 1.5,
    'Swiss': 1.5,
    'mozzarella': 1.5,
    'mayo': 1.25,
    'mustard': 1.25,
    'lettuce': 1.5,
    'tomato': 1.5
}

# Ask user for sandwich they preferences.
bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                            numbered=True, prompt='Select a bread type:\n')

protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                              numbered=True, prompt='Select a protein type:\n')

# Ask user if they want cheese.
cheese = pyip.inputYesNo('Would you like cheese? (Yes/No)\n')
cheese_type = None
if cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
                                 numbered=True, prompt='Select a cheese type:\n')
# Ask user if they want extras.
extras = pyip.inputYesNo('Would you like mayo, mustard, lettuce, or tomato? (Yes/No)\n')
extras_type = None
if extras == 'yes':
    extras_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'],
                                 numbered=True, prompt='Select a extras type:\n')

# Ask user how many sandwich they want.
quantity = pyip.inputInt('How many sandwiches would you like?\n', min=1)

# Calculate total cost.
total_cost = prices[bread_type] + prices[protein_type]
if cheese_type:
    total_cost += prices[cheese_type]
if extras_type:
    total_cost += prices[extras_type]

total_cost *= quantity

# Display choices and total cost.
print("\nYour choices:")
print(f"Bread: {bread_type}  - $ {prices[bread_type]:.2f}")   # Display Bread selected  and prices

print(f"Protein: {protein_type}  - $ {prices[protein_type]:.2f}")  # Display protein selected and prices
if cheese_type:
    print(f"Cheese: {cheese_type}  - $ {prices[cheese_type]:.2f}")  # Display cheese selected and prices

if extras_type:
    print(f"Extras: {extras_type}  - $ {prices[extras_type]:.2f}\n")  # Display extra selected item and prices

print(f"Quantity:   {quantity}")  # Display quantity of items.
print(f"Total cost:  - $ {total_cost}")  # Display of total amount.
