import read as r
import write as w
import purchase as p
import addProduct as ap

MakeChoice = "y"
while MakeChoice.lower()=="y":
    MakeChoice = "n"
    op = input("1: Add product\n2: Make bill\nEnter your choice: ")
    if '1'==str(op):
        print("\nAdd product\n")
        AddNewProduct = "y"
        while AddNewProduct.lower()=="y":
            ap.addproduct()
            AddNewProduct = input("\nDo you want to add more products?(y/n)\n")
        print("Products added :)")
            
    elif '2'==str(op):
        NewCustomerWaiting = "y"
        while NewCustomerWaiting.lower()=="y":
            a = r.readList()
            b = p.product(a)
            w.updateList(a,b)
            print("Invoice created\n")
            NewCustomerWaiting=input("Is any new customer waiting in the queue?(y/n): ")
        print("\nThankyou for shopping, Please visit again!")

    else:
        print("Invalid input! Please enter a valid input.")
        MakeChoice = "y"
