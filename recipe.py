class Recipe:
    """
    Base class for a bundt cake recipe.

    Attributes:
        name (str): Name of the recipe.
        ingredients (list): List of ingredients.
        base_cost (float): Base production cost per unit.
        complexity (int): Complexity score (1–10).
    """

    def __init__(self, name, ingredients, base_cost, complexity):
        self.name = name
        self.ingredients = ingredients
        self.base_cost = base_cost
        self.complexity = complexity

    def __str__(self):
        return (f"Recipe: {self.name}\n"
                f"  Ingredients: {', '.join(self.ingredients)}\n"
                f"  Base Cost: ${self.base_cost:.2f}\n"
                f"  Complexity: {self.complexity}/10")


class SeasonalRecipe(Recipe):
    """
    Represents a seasonal bundt cake recipe, only available
    during limited times.

    Attributes:
        season (str): Season of availability (e.g., Spring, Summer).
    """

    def __init__(self, name, ingredients, base_cost, complexity, season):
        super().__init__(name, ingredients, base_cost, complexity)
        self.season = season

    def __str__(self):
        return (super().__str__() +
                f"\n  Seasonal Availability: {self.season}")


class PremiumRecipe(Recipe):
    """
    Represents a premium bundt cake recipe with a price multiplier.

    Attributes:
        multiplier (float): The price markup applied to the base cost.
    """

    def __init__(self, name, ingredients, base_cost, complexity, multiplier):
        super().__init__(name, ingredients, base_cost, complexity)
        self.multiplier = multiplier

    def get_premium_price(self):
        return round(self.base_cost * self.multiplier, 2)

    def __str__(self):
        return (super().__str__() +
                f"\n  Premium Price: ${self.get_premium_price():.2f}")
