import read as r
import write as w
import purchase as p

NewCustomerWaiting = "y"
while NewCustomerWaiting.lower()=="y":
    a = r.readList()
    b = p.product(a)
    w.updateList(a,b)
    NewCustomerWaiting=input("Is any new customer waiting in the queue?(y/n): ")
print("\nThankyou for shopping, Please visit again!")
print("Please check the invoice created")