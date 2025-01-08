# Here your solution
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PaymentMethodInterface(ABC): 
    @abstractmethod
    def calculator_fee(self):
        pass

class CreditCard(PaymentMethodInterface):
    def __init__(self, amount):
        self.amount = amount

    def calculator_fee(self):
        fee = self.amount * 0.03
        logging.info(f"Calculated fee for Credit Card: {fee}")
        return fee
    

class PayPal(PaymentMethodInterface):
    def __init__(self, amount):
        self.amount = amount

    def calculator_fee(self):
        fee = self.amount * 0.05
        logging.info(f"Calculated fee for PayPal: {fee}")
        return fee
    
class BankTransfer(PaymentMethodInterface):
    def __init__(self, amount):
        self.amount = amount

    def calculator_fee(self):
        fee = self.amount * 2.5
        logging.info(f"Calculated fee for Bank Transfer: {fee}")
        return fee
    
class FeeCalculator:
    @staticmethod
    def calculator_fee(payment_method: PaymentMethodInterface):
        return payment_method.calculator_fee()
    

credit_card = CreditCard(100)
paypal = PayPal(100)
bank_transfer = BankTransfer(100)


FeeCalculator.calculator_fee(credit_card)  
FeeCalculator.calculator_fee(paypal)
FeeCalculator.calculator_fee(bank_transfer) 