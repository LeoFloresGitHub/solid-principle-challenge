
# Here your solution
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PaymentMethod(ABC):   
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalService(PaymentMethod):
    
    def pay(self,amount: float):
        logging.info(f"Paying {amount} using PayPal...")


class PaymentProcessor:
    def __init__(self, payment_service: PaymentMethod):
        self.payment_service = payment_service

    def process_payment(self, amount: float):
        self.payment_service.pay(amount)


paypal_service = PayPalService()
payment_processor = PaymentProcessor(paypal_service)
payment_processor.process_payment(100.0) 
