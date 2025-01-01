# Here your solution
from abc import ABC, abstractmethod

class PayInterface(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class RefundInterface(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class HandleDisputeInterface(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass


class BasicGiftCard(PayInterface):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")

class RefundableGiftCard(PayInterface, RefundInterface):
    def pay(self, amount: float) -> None:
        print(f"Refundable gift card used to pay {amount}.")
        
    def refund(self, amount: float) -> None:
        print(f"Refunded {amount} to the Refundable gift card.")
   

   
class PremiumGiftCard(PayInterface, RefundInterface,HandleDisputeInterface):
    def pay(self, amount: float) -> None:
        print(f"Refundable gift card used to pay {amount}.")
        
    def refund(self, amount: float) -> None:
        print(f"Refunded {amount} to the Refundable gift card.")
   
    def handle_dispute(self, dispute_id: str) -> None:
        raise NotImplementedError("Gift cards do not support disputes.")
