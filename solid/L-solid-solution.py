# Here your solution
from abc import ABC, abstractmethod

class RefundableInterface(ABC):
    def __init__(self, balance: float):
        self.balance = balance

    @abstractmethod
    def refund(self, amount: float):
        pass

class PayableAndRefundableInterface(RefundableInterface):
     
    @abstractmethod
    def pay(self, amount: float):
        pass
    

class PaymentMethod(PayableAndRefundableInterface):
    def __init__(self, balance: float):
        self.balance = balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
        self.balance += amount
        print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")


class NonRefundableGiftCard(RefundableInterface):
    def refund(self, amount: float):
        raise NotImplementedError(
            "NonRefundableGiftCard does not support refunds."
        )

        
# prueba = NonRefundableGiftCard(150)
# prueba.refund(20)