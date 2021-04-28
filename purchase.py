def product(List):
    L = List  
    a_name = input("Please enter your name: ")
    print("\nHello " + a_name + "! Welcome to our Electronic Store.\nLook at above and select product as your choice.")
    q = {}  
    flag = "Y"
    while flag.upper() == "Y": 
        product = input("\nWhat product do you want to buy? ")
        product_name = product.upper()  
        for l in L:
            if l[0].upper()==product_name:  
                p = True
                while p == True:
                    try:
                        p_quantity = int(input("How many " + product + " do you want to buy: "))
                        p = False
                    except: 
                        print("\t\tError!!!\nPlease enter integer value!! ")
                L_Q = int(l[2])
                if L_Q>=p_quantity:
                    q[product_name] = p_quantity
                else:
                    print(
                        "\nSorry! " + a_name + "!, " + product + " is out of stock.\n")

                flag = (input(a_name + " do you want buy more products?(Y/N)"))
                break
            elif str(L[-1][0]).upper()==str(l[0]).upper():
                print("Sorry! " + product + " is not available in our store.")
                print("\nChoose from following products please!")
                print("--------------------------------------------")
                print("PRODUCT\t\tPRICE\t\tQUANTITY")
                print("--------------------------------------------")
                for i in range(len(L)):
                    print(L[i][0], "\t\t", L[i][1], "\t\t", L[i][2])  
                print("--------------------------------------------")



    print("\nYou Choosed Items and it's Quantity respectively:")
    for i,j in q.items():
        print(i,j,sep="-")
    print("\n")

    f_amount = 0
    for keys in q.keys():
        for l in L:
            if keys == l[0].upper():
                p_price = int(l[1])
                p_num = int(q[keys])
                p_amount = (p_price * p_num)
                f_amount += (p_price * p_num)
                print("Total cost for",l[0],":" , p_amount)
                break
            

    total = f_amount
    print("Your payable amount is: ", total)

    import datetime  
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)  
    d = str(t) 
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)  
    e = str(u)  

    file = open(invoice + a_name + ".txt", "w")  
    file.write("=============================================================")
    file.write("\nELECTRONIC STORE\t\t\t\tINVOICE")
    file.write("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
    file.write("\nName of Customer: " + str(a_name) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for keys in q.keys():
        for l in L:
            if keys == str(l[0]).upper():
                file.write(
                    str("\n" + str(keys) + " \t\t " + str(q[str(l[0]).upper()]) + " \t\t " + str(l[1]) + " \t\t " + str( int(l[1])*int(q[keys]))))
                break
            
    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\t Your payable amount is: " + str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You " + a_name + " for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q
