from enum import Enum

class Foods(Enum):
    """
    An enumeration of different food categories.

    Attributes:
        NULL: Default; none set
        HOT_DOG: Hot Dog ($2.30)
        CORN_DOG: Corn Dog ($2.00)
        ICE_CREAM: Ice Cream ($3.00)
        ONION_RINGS: Onion Rings ($1.75)
        FRIES: French Fries ($1.50)
        TOTS: Tater Tots ($1.70)
        NACHOS: Nacho Chips ($1.90)
    """
    def __str__(self):
        return str(self.value)
    NULL = None
    HOT_DOG = "Hot Dog"
    CORN_DOG = "Corn Dog"
    ICE_CREAM = "Ice Cream"
    ONION_RINGS = "Onion Rings"
    FRIES = "French Fries"
    TOTS = "Tater Tots"
    NACHOS = "Nacho Chips"

class Topping(Enum):
    """
    An enumeration of different topping categories.

    Attributes:
        CHERRY: Cherry (Free)
        WHIPPED_CREAM: Whipped Cream (Free)
        KETCHUP: Ketchup (Free)
        MUSTARD: Mustard (Free)
        CHEESE: Nacho Cheese ($0.30)
        BACON: Bacon Bits ($0.30)
        CARAMEL: Caramel Sauce ($0.50)
        CHOCOLATE: Chocolate Sauce ($0.50)
        CHILI: Chili ($0.60)
    """
    def __str__(self):
        return str(self.value)
    CHERRY = "Cherry"
    WHIPPED_CREAM = "Whipped Cream"
    KETCHUP = "Ketchup"
    MUSTARD = "Mustard"
    CHEESE = "Nacho Cheese"
    BACON = "Bacon Bits"
    CARAMEL = "Caramel Sauce"
    CHOCOLATE = "Chocolate Sauce"
    CHILI = "Chili"

# Create class "Food"
class Food:
    """
    A class for storing a Food object.

    Attributes:
        _base (str): The base of the food (e.g., "Hot Dog", "Onion Rings"). Foods enums can also be used.
        _toppings (set): A set of toppings on the food (e.g., {"Cherry", "Chili"}).
    """

    _valid_bases = {"hot dog", "corn dog", "ice cream", "onion rings", "french fries", "tater tots", "nacho chips"}
    _valid_toppings = {"cherry", "whipped cream", "caramel sauce", "chocolate sauce", "nacho cheese", "chili", "bacon bits", "ketchup", "mustard"}

    def __init__(self):
        """
        Initializes an empty `Food` object.
        """
        self._base = Foods.NULL
        self._toppings = set()
        self._cost = 0.00
    
    # Return the _base property.
    def get_base(self):
        """
        Returns the base of the food.

        Returns:
            str: The base of the food.
        """
        return self._base
    
    # Return the _toppings property.
    def get_toppings(self):
        """
        Returns the toppings of the food as a list.

        Returns:
            list: A list of the food's toppings.
        """
        return list(self._toppings)
    
    # Return the number of toppings.
    def get_num_toppings(self):
        """
        Returns the number of toppings on the food.

        Returns:
            int: The number of toppings.
        """
        return len(self._toppings)

    # Set the food's _base property.
    def set_base(self, base):
        """
        Sets the base of the food.

        Args:
            base (str): The new base for the food. Valid bases are any Foods enum value aside from Foods.NULL.

        Raises:
            ValueError: If the base is invalid.
        """
        if base.value.casefold() in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Pick a proper base from {self._valid_bases}.")
    
    # Add a topping to the _toppings property.
    def add_topping(self, topping):
        """
        Adds a topping to the food.

        Args:
            topping (str): The topping to add. Valid topping are any Toppings enum.

        Raises:
            ValueError: If the topping is invalid.
        """
        if topping.value.casefold() in self._valid_toppings:
            self._toppings.add(topping.value)
        else:
            raise ValueError(f"Pick a proper topping from {self._valid_toppings}.")

    # Set the _toppings property to a given list.
    def set_toppings(self, toppings):
        """
        Sets the toppings on the food.

        Args:
            toppings (list): A list of toppings to set. Valid toppings are all Topping enums (e.g. Topping.CHERRY)

        Raises:
            ValueError: If any of the toppings are invalid.
        """
        for topping in toppings:
            if topping.value.casefold() not in self._valid_toppings:
                raise ValueError(f"Pick a proper topping from {self._valid_toppings}.")
        topping_set = set(toppings)
        for topping in topping_set:
            self._toppings.add(topping.value)
    
    def calculate_cost(self):
        """
        Calculates and returns the cost of the food.

        Returns:
            float: The cost of the food.
        """
        base_cost = 0.00
        topping_cost = 0.00
        match self._base:
            case Foods.HOT_DOG: base_cost = 2.30
            case Foods.CORN_DOG: base_cost = 2.00
            case Foods.ICE_CREAM: base_cost = 3.00
            case Foods.ONION_RINGS: base_cost = 1.75
            case Foods.FRIES: base_cost = 1.50
            case Foods.TOTS: base_cost = 1.70
            case Foods.NACHOS: base_cost = 1.90
        for topping in list(self._toppings):
            match topping:
                case Topping.CHERRY | Topping.WHIPPED_CREAM | Topping.KETCHUP | Topping.MUSTARD:
                    continue
                case Topping.CHEESE | Topping.BACON:
                    topping_cost += 0.30
                case Topping.CARAMEL | Topping.CHOCOLATE:
                    topping_cost += 0.50
                case Topping.CHILI:
                    topping_cost += 0.60
        return base_cost + topping_cost
