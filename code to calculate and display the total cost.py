class User:
    def __init__(self, user_id, name, email, address, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

    def register(self):
        print(f"User {self.name} registered.")

    def login(self):
        print(f"User {self.name} logged in.")

    def logout(self):
        print(f"User {self.name} logged out.")

    def update_profile(self, name=None, email=None, address=None, phone=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if address:
            self.address = address
        if phone:
            self.phone = phone
        print("Profile updated.")


class Product:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def view_details(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"

    def check_availability(self):
        return self.stock > 0


class ShoppingCart:
    def __init__(self, cart_id, user_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.items = {}  # {product_id: quantity}

    def add_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
        print(f"Added {quantity} of product {product_id} to cart.")

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print(f"Removed product {product_id} from cart.")
        else:
            print(f"Product {product_id} not in cart.")

    def update_quantity(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] = quantity
            print(f"Updated quantity of product {product_id} to {quantity}.")
        else:
            print(f"Product {product_id} not in cart.")

    def calculate_total_price(self, product_catalog):
        total_price = sum(product_catalog[pid].price * qty for pid, qty in self.items.items())
        return total_price


class Order:
    def __init__(self, order_id, user_id, cart_id, shipping_address):
        self.order_id = order_id
        self.user_id = user_id
        self.cart_id = cart_id
        self.shipping_address = shipping_address
        self.order_status = "Pending"

    def place_order(self):
        self.order_status = "Placed"
        print(f"Order {self.order_id} placed.")

    def cancel_order(self):
        self.order_status = "Cancelled"
        print(f"Order {self.order_id} cancelled.")

    def track_order(self):
        return f"Order {self.order_id} is {self.order_status}."


class Payment:
    def __init__(self, payment_id, order_id, payment_method):
        self.payment_id = payment_id
        self.order_id = order_id
        self.payment_method = payment_method
        self.payment_status = "Pending"

    def process_payment(self):
        self.payment_status = "Completed"
        print(f"Payment {self.payment_id} for Order {self.order_id} completed using {self.payment_method}.")

    def generate_receipt(self):
        return f"Receipt: Payment {self.payment_id}, Order {self.order_id}, Status: {self.payment_status}."


if __name__ == "__main__":
    # Create a user
    user = User(1, "Mupparaju Vinay", "mupparajuvinay@gmail.com", "123 Elm Street", "123-456-7890")
    user.register()
    user.login()

    # Create a product catalog
    product_catalog = {
        101: Product(101, "Laptop", "High-performance laptop", 1500, 10),
        102: Product(102, "Smartphone", "Latest smartphone", 800, 20),
        103: Product(103, "Headphones", "Wireless over-ear headphones", 200, 15),
        104: Product(104, "Smartwatch", "Feature-rich smartwatch", 300, 8)
    }

    # Display product catalog
    print("\nAvailable Products:")
    for product_id, product in product_catalog.items():
        print(product.view_details())

    # Create a shopping cart for the user
    cart = ShoppingCart(1, user.user_id)

    # Simulate adding items to the cart
    cart.add_item(101, 1)  # 1 Laptop
    cart.add_item(102, 2)  # 2 Smartphones
    cart.add_item(103, 1)  # 1 Headphones

    # Display items in the cart
    print("\nItems in the Cart:")
    for product_id, quantity in cart.items.items():
        product = product_catalog[product_id]
        print(f"{product.name}: {quantity} @ ${product.price} each")

    # Calculate total cost
    total_price = cart.calculate_total_price(product_catalog)
    print(f"\nTotal Price: ${total_price:.2f}")

    # Place an order
    order = Order(1, user.user_id, cart.cart_id, user.address)
    order.place_order()

    # Process payment
    payment = Payment(1, order.order_id, "Credit Card")
    payment.process_payment()

    # Display receipt
    print("\nReceipt:")
    print(payment.generate_receipt())