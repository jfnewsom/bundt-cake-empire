"""
lab05.py
Main script for the Bundt Cake Empire order system.
This script loads inventory, recipes, and orders, processes them,
and provides an interactive menu for business reporting.
"""

from store import BundtStore

# Named constants for file paths
INVENTORY_FILE = "bundt_inventory.txt"
RECIPES_FILE = "bundt_recipes.txt"
ORDER_FILE = "bundt_orders.txt"


def main():
    """
    Coordinates loading data, processing orders, and displaying menu options.
    """
    print("Welcome to the Bundt Cake Empire Order System!")

    # Initialize the store
    store = BundtStore(INVENTORY_FILE, RECIPES_FILE, ORDER_FILE)

    print("Processing orders...")
    store.process_orders()

    # Launch menu for viewing reports
    store.main_menu()


if __name__ == "__main__":
    main()
