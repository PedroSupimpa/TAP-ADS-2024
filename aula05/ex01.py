from abc import ABC, abstractmethod

class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantity * price for quantity, price in zip(self.quantities, self.prices))

class PaymentProcessing(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pay(self, security_code):
        pass

class CreditPayment(PaymentProcessing):
    def __init__(self, order: Order):
        super().__init__(order)
        print("Processing credit payment")

    def pay(self, security_code):
        self.order.status = 'paid'
        print("Payment processed successfully.")

class DebitPayment(PaymentProcessing):
    def __init__(self, order: Order):
        super().__init__(order)
        print("Processing debit payment")

    def pay(self, security_code):
        self.order.status = 'paid'
        print("Payment processed successfully.")

if __name__ == '__main__':
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("Mouse", 1, 50)
    order.add_item("Headset", 1, 50)
    print("Total price:", order.total_price())

    payment = CreditPayment(order=order)
    payment.pay("032564")
    print("Order status:", order.status)
