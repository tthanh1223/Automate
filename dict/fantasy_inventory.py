"""
Fantasy Game Inventory
You are creating a fantasy video game.
The data structure to model the player’s inventory will be a dictionary
where the keys are string values describing the item in the inventory.
The value is an integer value detailing how many of these items the player has.
For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.
"""
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print("Total number of items: " + str(item_total))
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby','bone','bone','bone','meat','meat','dragon heart']

# function to add items to the inventory
def addToInventory(inventory: dict, added_items: list):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1  # Count the specific item

addToInventory(inv, dragonLoot)
displayInventory(inv)


