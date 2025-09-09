class Shoe:
    """
    A class to represent a shoe product.

    Attributes:
        country (str): The country of the shoe's origin.
        code (str): The product code of the shoe.
        product (str): The name of the shoe product.
        cost (float): The cost of the shoe.
        quantity (int): The quantity of the shoe in stock.
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Returns the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Returns the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Returns a string representation of the Shoe object."""
        return (
            f"Country: {self.country}\n"
            f"Code: {self.code}\n"
            f"Product: {self.product}\n"
            f"Cost: ${self.cost:,.2f}\n"
            f"Quantity: {self.quantity}"
        )


shoes_list = []


def read_shoes_data(file_path="inventory.txt"):
"""
Reads shoe data from a file, creates Shoe objects, and appends them to shoes_list.
Handles file errors and skips the header line.
"""
try:
with open(file_path, "r", encoding="utf-8") as f:
lines = f.readlines()[1:] # Skip header line
for line in lines:
try:
country, code, product, cost, quantity = line.strip().split(',')
shoe = Shoe(country, code, product, cost, quantity)
shoes_list.append(shoe)
except ValueError as e:
print(f"Error parsing line: {line.strip()}. Details: {e}")
except FileNotFoundError:
print(f"Error: The file '{file_path}' was not found.")

def capture_shoes():
    """
    Allows a user to input data for a new shoe, creates a Shoe object,
    and appends it to shoes_list.
    """
    try:
        country = input("Enter the country: ")
        code = input("Enter the product code: ")
        product = input("Enter the product name: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        new_shoe = Shoe(country, code, product, cost, quantity)
        shoes_list.append(new_shoe)
        print("Shoe added successfully!")
    except ValueError:
        print("Invalid input. Please ensure cost is a number and quantity is an integer.")


def view_all():
    """Iterates through shoes_list and prints the details of each shoe."""
    if not shoes_list:
        print("No shoes in the inventory.")
        return

    print("\n--- All Shoes in Inventory ---")
    for shoe in shoes_list:
        print(shoe)
        print("-" * 25)

def re_stock():
    """
    Finds the shoe with the lowest quantity and asks the user to restock it.
    Updates the quantity in memory and in the inventory file.
    """
    if not shoes_list:
        print("No shoes to restock.")
        return

    lowest_qty_shoe = min(shoes_list, key=lambda x: x.get_quantity())
    print("\n--- Restock Needed ---")
    print("The following shoe has the lowest quantity and needs to be restocked:")
    print(lowest_qty_shoe)

    try:
        restock_amount = int(input("How many units would you like to add? "))
        lowest_qty_shoe.quantity += restock_amount
        print(f"Updated quantity for {lowest_qty_shoe.product}: {lowest_qty_shoe.quantity}")
        update_inventory_file()
    except ValueError:
        print("Invalid input. Please enter a valid integer for the restock amount.")


def search_shoe():
    """
    Searches for a shoe by its product code and prints its details if found.
    """
    code_to_search = input("Enter the product code to search for: ")
    found_shoe = None
    for shoe in shoes_list:
        if shoe.code.lower() == code_to_search.lower():
            found_shoe = shoe
            break
    
    if found_shoe:
        print("\n--- Shoe Found ---")
        print(found_shoe)
    else:
        print("No shoe with that code was found.")


def value_per_item():
    """Calculates and prints the total value for each shoe item."""
    if not shoes_list:
        print("No shoes in the inventory.")
        return

    print("\n--- Value per Item ---")
    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Product: {shoe.product} | Code: {shoe.code} | Value: ${value:,.2f}")


def highest_qty():
    """
    Finds the shoe with the highest quantity and prints that it is for sale.
    """
    if not shoes_list:
        print("No shoes in the inventory.")
        return

    highest_qty_shoe = max(shoes_list, key=lambda x: x.get_quantity())
    print("\n--- Highest Quantity Shoe ---")
    print(f"The product with the highest quantity is '{highest_qty_shoe.product}'.")
    print("It is now on sale!")
    print(highest_qty_shoe)

def update_inventory_file(file_path="inventory.txt"):
    """
    Updates the inventory file with the current data from shoes_list.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    except IOError:
        print(f"Error: Could not write to the file '{file_path}'.")

def display_menu(): 
    """
    Displays the user menu options.
    """
    print("\n--- Main Menu ---")     
    print("1. View all shoes")     
    print("2. Add a new shoe")     
    print("3. Restock lowest quantity shoe")     
    print("4. Search for a shoe by code")     
    print("5. Calculate and view value per item") 
    print("6. Find and mark highest quantity shoe for sale") 
    print("7. Exit")

def main():
    """Main function to run the inventory management system."""
    read_shoes_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            update_inventory_file()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()