class Customer:
    def __init__(self, customer_id, customer_name, contact_information, delivery_address):
        self.customer_id = customer_id
        self.customer_name = customer_name  # String
        self.contact_information = contact_information  # String
        self.delivery_address = delivery_address  # String

class Item:
    def __init__(self, item_id, name, description, unit_price, supplier_name):
        self.item_id = item_id
        self.name = name  # String
        self.description = description  # String
        self.unit_price = unit_price  # Double
        self.supplier_name = supplier_name  # String

class Supplier:
    def __init__(self, supplier_id, name, contact_information):
        self.supplier_id = supplier_id
        self.name = name  # String
        self.contact_information = contact_information  # String

class Billing:
    def __init__(self, billing_id, customer_id, payment_method, payment_amount):
        self.billing_id = billing_id
        self.customer_id = customer_id
        self.payment_method = payment_method  # String
        self.payment_amount = payment_amount  # Double
        self.payment_status = "Pending"

    def process_payment(self):
        self.payment_status = "Completed"

    def generate_receipt(self):
        return f"\nReceipt: \nCustomer ID: {self.customer_id}\nPayment Method: {self.payment_method}\nAmount: ${self.payment_amount}\nStatus: {self.payment_status}"

class Shipping:
    def __init__(self, shipping_id, customer_id, delivery_address, shipping_method):
        self.shipping_id = shipping_id
        self.customer_id = customer_id
        self.delivery_address = delivery_address  # String
        self.shipping_method = shipping_method  # String
        self.shipping_status = "Pending"

    def ship_order(self):
        self.shipping_status = "Shipped"

    def track_order(self):
        return f"\nShipping Info: \nCustomer ID: {self.customer_id}\nDelivery Address: {self.delivery_address}\nMethod: {self.shipping_method}\nStatus: {self.shipping_status}"

if __name__ == "__main__":
    customer = Customer(1, "Vinay", "vinay@gmail.com", "123 Elm Street")
    print(f"Customer: {customer.customer_name}, Contact: {customer.contact_information}")

    supplier1 = Supplier(1, "Tech Supplies", "techsupplier@gmail.com")
    supplier2 = Supplier(2, "Office World", "officeworld@gmail.com")
    print(f"Supplier: {supplier1.name}, Contact: {supplier1.contact_information}")
    print(f"Supplier: {supplier2.name}, Contact: {supplier2.contact_information}")

    item1 = Item(101, "Laptop", "High-performance laptop", 2000.0, supplier1.name)
    item2 = Item(102, "Keyboard", "Mechanical keyboard", 150.0, supplier2.name)
    item3 = Item(103, "Mouse", "Wireless mouse", 50.0, supplier2.name)

    shopping_cart = {
        item1.item_id: {"item": item1, "quantity": 1},
        item2.item_id: {"item": item2, "quantity": 1},
        item3.item_id: {"item": item3, "quantity": 1}
    }

    total_cost = sum(data["item"].unit_price * data["quantity"] for data in shopping_cart.values())

    print("\nItems Purchased:")
    for data in shopping_cart.values():
        item = data["item"]
        quantity = data["quantity"]
        print(f"{item.name} - Unit Price: ${item.unit_price} x Quantity: {quantity} = ${item.unit_price * quantity}")

    print(f"\nTotal Cost: ${total_cost}")

    billing = Billing(1, customer.customer_id, "Credit Card", total_cost)
    billing.process_payment()
    print(billing.generate_receipt())

    shipping = Shipping(1, customer.customer_id, customer.delivery_address, "Express")
    shipping.ship_order()
    print(shipping.track_order())
