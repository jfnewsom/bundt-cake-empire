class Cake:
    """
    Represents a bundt cake with a name, price, and ingredients.
    """

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients

    def __str__(self):
        """
        Returns a formatted string representing the cake's recipe card.
        """
        output = f"\n{'-' * 40}\n🍰 {self.name} Recipe Card\n{'-' * 40}\n"
        output += f"Price: ${self.price:.2f}\n"
        output += "Ingredients:\n"
        for ingredient in self.ingredients:
            output += f"- {ingredient}\n"
        return output


class MiniBundtCake(Cake):
    """
    Represents a mini bundt cake with a reduced ingredient list and price.
    """

    def __init__(self, name, price, ingredients):
        mini_ingredients = {k: max(1, v // 2) for k, v in ingredients.items()}
        mini_price = round(price * 0.6, 2)
        super().__init__(f"{name} (Mini)", mini_price, mini_ingredients)


class PremiumBundtCake(Cake):
    """
    Represents a premium bundt cake with increased price and ingredients.
    """

    def __init__(self, name, price, ingredients):
        premium_ingredients = {k: int(v * 1.5) for k, v in ingredients.items()}
        premium_price = round(price * 1.4, 2)
        super().__init__(f"{name} (Premium)", premium_price, premium_ingredients)


class CakeFactory:
    """
    Loads recipes from a file and produces Cake objects or subclasses.
    """

    def __init__(self, recipe_file):
        self.recipes = {}
        self.load_recipes(recipe_file)

    def load_recipes(self, filename):
        """
        Loads cake recipes from a text file into the recipe dictionary.
        Format: CakeName,Price,Ingredient1,Qty1,Ingredient2,Qty2,...
        """
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(',')
                if len(parts) < 3:
                    continue
                name = parts[0].strip()
                try:
                    price = float(parts[1])
                except ValueError:
                    continue
                ingredients = {}
                for i in range(2, len(parts), 2):
                    try:
                        ing = parts[i].strip()
                        amt = int(parts[i + 1])
                        ingredients[ing] = amt
                    except (IndexError, ValueError):
                        continue
                self.recipes[name.lower()] = Cake(name, price, ingredients)

    def get_cake(self, name):
        """
        Returns a Cake object or subclass matching the given name.
        Name matching is case-insensitive. Handles Mini and Premium variants.
        """
        name = name.strip()
        lname = name.lower()

        if lname.endswith("(mini)"):
            base_name = name[:-6].strip().lower()
            if base_name in self.recipes:
                base = self.recipes[base_name]
                return MiniBundtCake(base.get_name(), base.get_price(), base.get_ingredients())
        elif lname.endswith("(premium)"):
            base_name = name[:-9].strip().lower()
            if base_name in self.recipes:
                base = self.recipes[base_name]
                return PremiumBundtCake(base.get_name(), base.get_price(), base.get_ingredients())
        elif lname in self.recipes:
            return self.recipes[lname]
        return None

    def get_all_recipes(self):
        """
        Returns the dictionary of all cake recipes in the factory.
        """
        return self.recipes
