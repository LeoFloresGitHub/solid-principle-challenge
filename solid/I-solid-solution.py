# Here your solution
from abc import ABC, abstractmethod
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
        logging.info(f"Gift card used to pay {amount}.")

class RefundableGiftCard(PayInterface, RefundInterface):
    def pay(self, amount: float) -> None:
        logging.info(f"Refundable gift card used to pay {amount}.")
        
    def refund(self, amount: float) -> None:
        logging.info(f"Refunded {amount} to the Refundable gift card.")
   
class PremiumGiftCard(PayInterface, RefundInterface,HandleDisputeInterface):
    def pay(self, amount: float) -> None:
        logging.info(f"Refundable gift card used to pay {amount}.")
        
    def refund(self, amount: float) -> None:
        logging.info(f"Refunded {amount} to the Refundable gift card.")
   
    def handle_dispute(self, dispute_id: str) -> None:
        logging.info(f"Dispute {dispute_id} is being handled by the Premium Gift Card support team.")


basic_card = BasicGiftCard()
basic_card.pay(50.0)

refundable_card = RefundableGiftCard()
refundable_card.refund(50.0)

premium_card = PremiumGiftCard()
premium_card.handle_dispute(545887)