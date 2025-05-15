"""
orders.py

Defines the CakeOrder class and a helper function to load orders from a file.
"""


class CakeOrder:
    """
    Represents a customer's bundt cake order.

    Attributes:
        customer_name (str): Name of the customer placing the order.
        cake_type (str): The type of bundt cake being ordered.
        quantity (int): The number of cakes ordered.
    """

    def __init__(self, customer_name, cake_type, quantity):
        """
        Initializes a CakeOrder object with customer name, cake type,
        and quantity.

        Args:
            customer_name (str): The name of the customer.
            cake_type (str): The cake variety being ordered.
            quantity (int): How many cakes the customer wants.
        """
        self.__customer_name = customer_name
        self.__cake_type = cake_type
        self.__quantity = quantity

    def get_customer_name(self):
        """Returns the customer's name."""
        return self.__customer_name

    def get_cake_type(self):
        """Returns the type of cake ordered."""
        return self.__cake_type

    def get_quantity(self):
        """Returns the quantity ordered."""
        return self.__quantity

    def __str__(self):
        """
        Returns a formatted string describing the cake order.
        """
        return (
            f"{self.__customer_name} ordered "
            f"{self.__quantity} x {self.__cake_type}"
        )


def load_orders(filename):
    """
    Loads customer cake orders from a text file and returns a list of
    CakeOrder objects.

    Args:
        filename (str): The path to the file containing order data.

    Returns:
        list: A list of CakeOrder objects created from the file.
    """
    orders = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                tokens = line.split(',')
                if len(tokens) != 3:
                    print(f"Skipping malformed line: {line}")
                    continue
                customer_name = tokens[0].strip()
                cake_type = tokens[1].strip()
                try:
                    quantity = int(tokens[2].strip())
                    order = CakeOrder(customer_name, cake_type, quantity)
                    orders.append(order)
                except ValueError:
                    print(f"Invalid quantity in line: {line}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return orders
