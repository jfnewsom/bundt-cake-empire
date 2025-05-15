from inventory import CakeInventory
from cake import CakeFactory
from orders import load_orders

class BundtStore:
    def __init__(self, inventory_file, recipe_file, order_file):
        self.inventory = CakeInventory.from_file(inventory_file)
        self.factory = CakeFactory(recipe_file)
        self.orders = load_orders(order_file)
        self.fulfilled_orders = []
        self.missed_orders = []
        self.total_revenue = 0.0
        self.total_cost = 0.0

    def process_orders(self):
        for order in self.orders:
            cake = self.factory.get_cake(order.get_cake_type())
            if not cake:
                print(f"Unknown cake type: {order.get_cake_type()}")
                self.missed_orders.append(order)
                continue

            success, cost = self.inventory.deduct_ingredients(cake.get_ingredients(), order.get_quantity())
            if success:
                self.fulfilled_orders.append((order, cake))
                self.total_revenue += cake.get_price() * order.get_quantity()
                self.total_cost += cost
            else:
                self.missed_orders.append(order)

    def generate_inventory_report(self):
        print("\n--- Inventory Report ---")
        inventory_data = self.inventory.get_all_items()
        if not isinstance(inventory_data, dict):
            print("Error: Inventory data is not in the expected format.")
            return
        for ingredient, (qty, cost) in inventory_data.items():
            print(f"{ingredient:<25} {qty} units @ ${cost:.2f}/unit")

    def generate_fulfilled_orders_report(self):
        print("\n--- Fulfilled Orders ---")
        if not self.fulfilled_orders:
            print("No orders were fulfilled.")
        for order, cake in self.fulfilled_orders:
            print(f"{order.get_customer_name():<20} - {order.get_cake_type()} x{order.get_quantity()}")

    def generate_missed_orders_report(self):
        print("\n--- Missed Orders ---")
        if not self.missed_orders:
            print("All orders were fulfilled!")
        for order in self.missed_orders:
            print(f"{order.get_customer_name():<20} - {order.get_cake_type()} x{order.get_quantity()}")

    def generate_sales_summary(self):
        print("\n--- Sales Summary ---")
        print(f"Total Revenue: ${self.total_revenue:.2f}")
        print(f"Total Cost:    ${self.total_cost:.2f}")
        print(f"Net Profit:    ${self.total_revenue - self.total_cost:.2f}")

    def view_recipes(self):
        print("\n--- Recipe List ---")
        recipes = self.factory.get_all_recipes()
        recipe_names = list(recipes.keys())
        for i, name in enumerate(recipe_names, start=1):
            print(f"{i}. {name}")

        try:
            choice = int(input("\nSelect a cake number to view its recipe (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(recipe_names):
                selected_name = recipe_names[choice - 1]
                cake = recipes[selected_name]
                print("\n" + "-" * 40)
                print(f"🍰 {cake.get_name().title()} Recipe Card")
                print("-" * 40)
                print(f"Price: ${cake.get_price():.2f}")
                print("Ingredients:")
                for ingredient, amount in cake.get_ingredients().items():
                    print(f"  - {ingredient.title()}: {amount}")
                print("-" * 40)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    def main_menu(self):
        while True:
            print("\nBundt Cake Empire - Main Menu")
            print("1. View Inventory Report")
            print("2. View Fulfilled Orders")
            print("3. View Missed Orders")
            print("4. View Sales Summary")
            print("5. View Recipes")
            print("Q. Quit")

            choice = input("Enter your choice: ").strip().lower()
            if choice == '1':
                self.generate_inventory_report()
            elif choice == '2':
                self.generate_fulfilled_orders_report()
            elif choice == '3':
                self.generate_missed_orders_report()
            elif choice == '4':
                self.generate_sales_summary()
            elif choice == '5':
                self.view_recipes()
            elif choice == 'q':
                print("Exiting the Bundt Cake Empire Order System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")