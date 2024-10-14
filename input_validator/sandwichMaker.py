# Write a program that asks users for their sandwich preferences.
# The program should use PyInputPlus to ensure that they enter valid input, such as:
# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
# Come up with prices for each of these options,
# and have your program display a total cost after the user enters their selection.

import pyinputplus as pyip
# Price for options
BREAD_TYPES = {'wheat': 15, 'white': 20, 'sourdough': 30}
PROTEIN_TYPES = {'chicken': 25, 'turkey': 30, 'ham': 20, 'tofu': 15}
CHEESE_TYPES = {'cheddar': 10, 'Swiss': 12, 'mozzarella': 8}
CONDIMENTS_PRICE = {'mayo': 2, 'mustard': 2, 'lettuce': 3, 'tomato': 3}

# get input
print("Welcome to the Sandwich Order System!".center(50, '-'))
bread = pyip.inputMenu(['wheat','white','sourdough'],'What is your bread?\n')
protein = pyip.inputMenu(['chicken','turkey','tofu','ham'],'What is your protein?\n')
cheese_or_not = pyip.inputYesNo("Do you want cheese?")
cheese = None
if cheese_or_not == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],"What is your cheese?\n")
mayo_or_not = pyip.inputYesNo("Do you want a mayo?")
mustard_or_not = pyip.inputYesNo("Do you want a mustard?")
lettuce_or_not = pyip.inputYesNo("Do you want a lettuce?")
tomato_or_not = pyip.inputYesNo("Do you want a tomato?")
how_many = pyip.inputInt("How many cheeses do you want?",min = 1)

# Calculating the total price:
total_price = BREAD_TYPES.get(bread) + PROTEIN_TYPES.get(protein)
if cheese:
    total_price += CHEESE_TYPES.get(cheese)
if mayo_or_not == 'yes':
    total_price += CONDIMENTS_PRICE.get('mayo')
if mustard_or_not == 'yes':
    total_price += CONDIMENTS_PRICE['mustard']
if lettuce_or_not == 'yes':
    total_price += CONDIMENTS_PRICE['lettuce']
if tomato_or_not == 'yes':
    total_price += CONDIMENTS_PRICE['tomato']

total_price *= how_many

print(f"\nYour total price for {how_many} sandwich(es) is: ${total_price}")



