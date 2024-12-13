from enum import Enum

# Drink assets
from ..api.drinks import Drink
from ..api.drinks import Size

# Food assets
from ..api.food import Food
from ..api.food import Foods
from ..api.food import Topping

# Blizzard assets
from ..api.blizzard import Blizzard
from ..api.blizzard import BlizzardFlavor
from ..api.blizzard import BlizzardTopping

# Order assets
from ..api.orders import Order

import unittest

class MethodTests(unittest.TestCase):

    def test_drink(self):
        item = Drink(Size.SMALL)
        item.set_base("Sprite")
        item.set_flavors({"Lemon", "Cherry"})
        item.add_flavor("Lime")
        self.assertEqual(item.calculate_cost(), 1.50 + 0.15 * 3)

    def test_food(self):
        item = Food()
        item.set_base(Foods.HOT_DOG)
        item.set_toppings({Topping.BACON, Topping.CHEESE})
        item.add_topping(Topping.CHILI)
        item.add_topping(Topping.KETCHUP)
        self.assertEqual(item.calculate_cost(), 3.50, "This food item should be $3.50.")
    
    def test_blizzard(self):
        item = Blizzard()
        item.set_base(BlizzardFlavor.SMORE)
        item.set_toppings({BlizzardTopping.CHOCOLATE, BlizzardTopping.CARAMEL})
        item.add_topping(BlizzardTopping.OREO)
        item.add_topping(BlizzardTopping.WHIPPED_CREAM)
        self.assertEqual(item.calculate_cost(), 6.00, "This item should be $6.00.")
    
    def test_order(self):
        order = Order()

        item = Drink(Size.SMALL)
        item.set_base("Sprite")
        item.set_flavors({"Lemon", "Cherry"})
        item.add_flavor("Lime")
        order.add_item(item)

        item = Food()
        item.set_base(Foods.HOT_DOG)
        item.set_toppings({Topping.BACON, Topping.CHEESE})
        item.add_topping(Topping.CHILI)
        item.add_topping(Topping.KETCHUP)
        order.add_item(item)

        item = Blizzard()
        item.set_base(BlizzardFlavor.SMORE)
        item.set_toppings({BlizzardTopping.CHOCOLATE, BlizzardTopping.CARAMEL})
        item.add_topping(BlizzardTopping.OREO)
        item.add_topping(BlizzardTopping.WHIPPED_CREAM)
        order.add_item(item)
        
        print(order.get_receipt())

test = MethodTests()
test.test_order()
