# OOPS: Object-Oriented Programming system

# Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"paid ₹{amount} using credit card")
    
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"paid ₹{amount} using UPI")



p1= CreditCardPayment()
p1.pay(1000)
p2= UPIPayment()
p2.pay(500)