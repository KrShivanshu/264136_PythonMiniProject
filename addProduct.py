def addproduct():
    file = open("ProductList.txt", "r")  
    lines = file.readlines()
    L = []
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()

    p_name = input("Enter the product name: ")
    p_price = int(input("Enter the price: "))
    p_quantity = int(input("Enter the quantity: "))

    for l in L:
        if str(l[0]).upper()==p_name.upper():
            l[1]=str(p_price)
            l[2]=str(int(l[2])+int(p_quantity))
            break
        elif str(L[-1][0]).upper()==str(l[0]).upper():
            L.append([p_name,str(p_price),str(p_quantity)])
    
    files = open("ProductList.txt", "w") 
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    