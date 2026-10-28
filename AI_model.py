from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class JazzCashPayment(Payment):
    def pay(self, amount):
        return f"Paid RS. {amount} using Jazzcash."
class EasyPaisaPayment(Payment):
    def pay(self, amount):
        return f"Paid RS. {amount} using Easypaisa."

jazzpament = JazzCashPayment()
easypaisa = EasyPaisaPayment()
easy = easypaisa.pay(3000)
jazz = jazzpament.pay(2000)
print(jazz)
print(easy) 