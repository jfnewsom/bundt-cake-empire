class CakeInventory:
    def __init__(self, inventory_data):
        if not isinstance(inventory_data, dict):
            raise TypeError("Expected a dictionary for inventory data.")
        self._inventory = inventory_data

    def has_ingredients(self, required_ingredients, quantity):
        for ingredient, amount_needed in required_ingredients.items():
            total_required = amount_needed * quantity
            available_qty = self._inventory.get(ingredient, (0, 0.0))[0]
            if available_qty < total_required:
                return False
        return True

    def deduct_ingredients(self, required_ingredients, quantity):
        """
        Attempts to deduct the required ingredients from the inventory.
        Returns (True, cost) if successful, or (False, 0.0) if any ingredient is insufficient.
        """
        # First check if all required ingredients are available in sufficient quantity
        for ingredient, amount_per_cake in required_ingredients.items():
            if ingredient not in self._inventory:
                print(f"[DEBUG] Missing ingredient: {ingredient}")
                return False, 0.0
            current_qty = self._inventory[ingredient][0]
            if current_qty < amount_per_cake * quantity:
                print(f"[DEBUG] Not enough {ingredient}: needed {amount_per_cake * quantity}, available {current_qty}")
                return False, 0.0

        # Deduct ingredients and calculate cost
        total_cost = 0.0
        for ingredient, amount_per_cake in required_ingredients.items():
            total_amount = amount_per_cake * quantity
            current_qty, unit_cost = self._inventory[ingredient]
            self._inventory[ingredient] = (current_qty - total_amount, unit_cost)
            total_cost += total_amount * unit_cost

        print(f"[DEBUG] Deducted ingredients for {quantity} cake(s): cost = ${total_cost:.2f}")
        return True, total_cost

    def get_all_items(self):
        return self._inventory

    @classmethod
    def from_file(cls, filename):
        inventory_data = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split(',')
                    if len(parts) != 3:
                        continue
                    name, qty, cost = parts
                    try:
                        inventory_data[name.strip()] = (int(qty), float(cost))
                    except ValueError:
                        continue
        except Exception as e:
            raise ValueError(f"Error reading inventory file: {e}")
        print("[DEBUG] Parsed inventory data:")
        for k, v in inventory_data.items():
            print(f"  {k}: qty={v[0]}, cost={v[1]}")
        return cls(inventory_data)