from enum import Enum

class BlizzardFlavor(Enum):
    """
    An enumeration of different Blizzard flavors.
    
    Attributes:
        NULL: Default; none set.
        VANILLA: Vanilla Bean ($3.00)
        CHOCOLATE: Chocolate ($3.00)
        BANANA: Banana ($3.50)
        BUTTER_PECAN: Butter Pecan ($3.50)
        MINT_CHIP: Mint Chocolate Chip ($4.00)
        SMORE: S'more ($4.00)
    """
    def __str__(self):
        return str(self.value)
    NULL = None
    VANILLA = "Vanilla Bean"
    CHOCOLATE = "Chocolate"
    BANANA = "Banana"
    BUTTER_PECAN = "Butter Pecan"
    MINT_CHIP = "Mint Chocolate Chip"
    SMORE = "S'more"

class BlizzardTopping(Enum):
    """
    An enumeration of different topping categories.

    Attributes:
        CHERRY: Cherry (Free)
        WHIPPED_CREAM: Whipped Cream (Free)
        CARAMEL: Caramel Sauce ($0.50)
        CHOCOLATE: Chocolate Sauce ($0.50)
        PECANS: Pecans ($0.50)
        OREO: Oreos ($1.00)
        KITKAT: Kit-Kats ($1.00)
        MMS: M&Ms ($1.00)
        COOKIE_DOUGH: Cookie Dough ($1.00)
    """
    def __str__(self):
        return str(self.value)
    CHERRY = "Cherry"
    WHIPPED_CREAM = "Whipped Cream"
    CARAMEL = "Caramel Sauce"
    CHOCOLATE = "Chocolate Sauce"
    PECANS = "Pecans"
    OREO = "Oreos"
    KITKAT = "KitKats"
    MMS = "M&Ms"
    COOKIE_DOUGH = "Cookie Dough"

# Create class "Blizzard"
class Blizzard:
    """
    A class for storing a Blizzard object.

    Attributes:
        _base (str): The base flavor of the Blizzard (e.g., "Vanilla Bean", "S'more"). BlizzardFlavor enums can also be used.
        _toppings (set): A set of flavors in the drink (e.g., {"Lemon", "Cherry"}).
    """

    _valid_bases = {"vanilla bean", "chocolate", "banana", "butter pecan", "s'more", "mint chocolate chip"}
    _valid_toppings = {"cherry", "whipped cream", "caramel sauce", "chocolate sauce", "oreos", "kitkats", "m&ms", "cookie dough", "pecans"}

    def __init__(self):
        """
        Initializes an empty `Blizzard` object.
        """
        self._base = BlizzardFlavor.NULL
        self._toppings = set()
        self._cost = 0.00
    
    # Return the _base property.
    def get_base(self):
        """
        Returns the base of the Blizzard.

        Returns:
            str: The base of the Blizzard.
        """
        return self._base
    
    # Return the _toppings property.
    def get_toppings(self):
        """
        Returns the toppings of the Blizzard as a list.

        Returns:
            list: A list of the Blizzard's toppings.
        """
        return list(self._toppings)
    
    # Return the number of toppings.
    def get_num_toppings(self):
        """
        Returns the number of toppings in the Blizzard.

        Returns:
            int: The number of toppings.
        """
        return len(self._toppings)

    # Set the Blizzard's _base property.
    def set_base(self, base):
        """
        Sets the base of the Blizzard.

        Args:
            base (str): The new base for the Blizzard. Valid bases are any BlizzardFlavor enum value aside from BlizzardFlavor.NULL.

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
        Adds a topping to the Blizzard.

        Args:
            topping (str): The topping to add. Valid topping are any BlizzardToppings enum.

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
        Sets the toppings on the Blizzard.

        Args:
            toppings (list): A list of toppings to set. Valid toppings are all BlizzardTopping enums (e.g. BlizzardTopping.CHERRY)

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
        Calculates and returns the cost of the Blizzard.

        Returns:
            float: The cost of the Blizzard.
        """
        base_cost = 0.00
        topping_cost = 0.00
        match self._base:
            case BlizzardFlavor.VANILLA | BlizzardFlavor.CHOCOLATE:
                base_cost = 3.00
            case BlizzardFlavor.BANANA | BlizzardFlavor.BUTTER_PECAN:
                base_cost = 3.50
            case BlizzardFlavor.SMORE | BlizzardFlavor.MINT_CHIP:
                base_cost = 4.00
        for topping in list(self._toppings):
            match topping:
                case BlizzardTopping.CHERRY | BlizzardTopping.WHIPPED_CREAM:
                    continue
                case BlizzardTopping.CARAMEL | BlizzardTopping.CHOCOLATE | BlizzardTopping.PECANS:
                    topping_cost += 0.50
                case BlizzardTopping.OREO | BlizzardTopping.KITKAT | BlizzardTopping.MMS | BlizzardTopping.COOKIE_DOUGH:
                    topping_cost += 1.00
        return base_cost + topping_cost
