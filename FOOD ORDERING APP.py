import json

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Admin(User):
    def register(self):
        admin_data = {"name": self.name, "email": self.email, "password": self.password}
        with open("admin.json", "w") as file:
            json.dump(admin_data, file)
            print("Admin registered successfully!")

    def login(self):
        try:
            with open("admin.json", "r") as file:
                admin_data = json.load(file)
                if admin_data["email"] == self.email and admin_data["password"] == self.password:
                    print("Admin login successful!")
                    return True
                else:
                    print("Invalid credentials!")
                    return False
        except FileNotFoundError:
            print("Admin not found!")
            return False

    def view_menu(self, menu):
        print("\nFood Menu:")
        for item_key, item in menu.items():
            print(f"{item_key}. {item['name']} - ${item['price']}")

    def add_food_item(self, menu):
        pass

    def update_food_item(self, menu):
        pass

    def delete_food_item(self, menu):
        pass

class Customer(User):
    def __init__(self, name, email, password, phone_number, address):
        super().__init__(name, email, password)
        self.phone_number = phone_number
        self.address = address
        self.order_history = []

    def register(self):
        customer_data = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "address": self.address,
            "order_history": []
        }
        with open("customer.json", "w") as file:
            json.dump(customer_data, file)
        print("Registration successful!")

    def login(self):
        try:
            with open("customer.json", "r") as file:
                customer_data = json.load(file)
                if (
                    self.email == customer_data["email"]
                    and self.password == customer_data["password"]
                ):
                    print("Login successful!")
                    return True
                else:
                    print("Invalid email or password!")
                    return False
        except FileNotFoundError:
            print("Customer not found!")
            return False

    def view_menu(self, menu):
        pass

    def place_order(self, menu, order_history):
        pass

    def view_order_history(self, order_history):
        pass

    def update_profile(self):
        pass

menu = {
    "1": {"name": "Burger", "price": 5.99, "quantity": 10, "discount": 0, "stock": 10},
    "2": {"name": "Pizza", "price": 8.99, "quantity": 8, "discount": 5, "stock": 8},
}
order_history = []

while True:
    print("\n1. Admin")
    print("2. Customer")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        admin_email = input("Enter your email: ")
        admin_password = input("Enter your password: ")
        admin = Admin("", admin_email, admin_password)
        if admin.login():
            while True:
                print("\nAdmin Menu:")
                print("1. View Food Menu")
                print("2. Add Food Item")
                print("3. Update Food Item")
                print("4. Delete Food Item")
                print("5. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    admin.view_menu(menu)
                elif admin_choice == "2":
                    admin.add_food_item(menu)
                elif admin_choice == "3":
                    admin.update_food_item(menu)
                elif admin_choice == "4":
                    admin.delete_food_item(menu)
                elif admin_choice == "5":
                    print("Admin logged out successfully!")
                    break
                else:
                    print("Invalid choice!")

    elif choice == "2":
        customer_email = input("Enter your email: ")
        customer_password = input("Enter your password: ")
        customer = Customer("", customer_email, customer_password, "", "")
        if customer.login():
            while True:
                print("\nCustomer Menu:")
                print("1. View Food Menu")
                print("2. Place Order")
                print("3. View Order History")
                print("4. Update Profile")
                print("5. Logout")

                customer_choice = input("Enter your choice: ")

                if customer_choice == "1":
                    customer.view_menu(menu)
                elif customer_choice == "2":
                    customer.place_order(menu, order_history)
                elif customer_choice == "3":
                    customer.view_order_history(order_history)
                elif customer_choice == "4":
                    customer.update_profile()
                elif customer_choice == "5":
                    print("Customer logged out successfully!")
                    break
                else:
                    print("Invalid choice!")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
