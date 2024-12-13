from enum import Enum

# Drink assets
from drinks import Drink
from drinks import Size

# Food assets
from food import Food
from food import Foods
from food import Topping

# Blizzard assets
from blizzard import Blizzard
from blizzard import BlizzardFlavor
from blizzard import BlizzardTopping

import unittest

# Create class "Order"
class Order:
    """
    A class representing an order of drinks, food, or Blizzards.

    Attributes:
        _items (list): A list of `Drink`, `Food`, or `Blizzard` objects in the order.
    """
    # Give the class instance its _items property.
    def __init__(self):
        """Initializes an empty order."""
        self._items = []
    
    # Return the list of items in this instance.
    def get_items(self):
        """
        Returns a list of `Drink`, `Food`, or `Blizzard` objects in the order.

        Returns:
            list: A list of `Drink`, `Food`, or `Blizzard` objects.
        """
        return self._items

    # Return the number of items in this instance.
    def get_total(self):
        """
        Returns the total number of items in the order.

        Returns:
            int: The number of items in the order.
        """
        return len(self._items)
    
    # List out every item in the list.
    def get_receipt(self):
        """
        Generates a formatted receipt for the order.

        Returns:
            str: A formatted string representing the receipt.
        """
        receipt = "Your order receipt:\n"
        for i, item in enumerate(self._items):
            if isinstance(item, Drink):
                base = item.get_base()
                # Formats the "flavors" string like "Lemon, Mint, Blueberry"
                flavors = ", ".join(item.get_flavors())

                price = item.calculate_cost()
                # Example: "1: Base - Root Beer, Flavors - Lemon, Cherry"
                receipt += f"{i + 1}: Base - {base}, Flavors - {flavors}, Price - ${price}\n"
            elif isinstance(item, (Food, Blizzard)):
                base = item.get_base()
                # Formats the "flavors" string like "Lemon, Mint, Blueberry"
                flavors = ", ".join(item.get_toppings())

                price = item.calculate_cost()
                # Example: "1: Base - Root Beer, Flavors - Lemon, Cherry"
                receipt += f"{i + 1}: Base - {base}, Toppings - {flavors}, Price - ${price}\n"
        return receipt
    
    # Add a Drink instance to the end of the list.
    def add_item(self, item):
        """
        Adds a `Drink`, `Food`, or `Blizzard` object to the order.

        Args:
            item (Drink, Food, or Blizzard): The `Drink`, `Food`, or `Blizzard` object to add.

        Raises:
            ValueError: If the argument is not a `Drink`, `Food`, or `Blizzard` object.
        """
        if isinstance(item, (Drink, Food, Blizzard)):
            self._items.append(item)
        else:
            # If the instance is not a Drink, Food, or Blizzard, throw an error.
            raise ValueError("You can only add drinks, food, or Blizzards to this order.")
    
    # Remove a Drink instance from the list based on index.
    def remove_item(self, index):
        """
        Removes a `Drink`, `Food`, or `Blizzard` object from the order at the specified index.

        Args:
            index (int): The index of the item to remove.

        Raises:
            IndexError: If the index is invalid.
        """
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            # If the index is outside of the list, i.e. invalid, throw an error.
            raise IndexError("Invalid index, cannot remove item.")