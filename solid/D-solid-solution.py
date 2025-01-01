
# Here your solution
from abc import ABC, abstractmethod

class PaymentMethod(ABC):  # Abstracción (Interfaz)
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalService(PaymentMethod):
    
    def pay(self,amount: float):
        print(f"Paying {amount} using PayPal...")


class PaymentProcessor:
    def __init__(self, paypal_service: PayPalService):
        self.paypal_service = paypal_service

    def process_payment(self, amount: float):
        self.paypal_service.pay(amount)

