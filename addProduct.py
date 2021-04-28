def addproduct():
    file = open("ProductList.txt", "r")  
    lines = file.readlines()
    L = []
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()

    L.append([input("Enter the product name: "),(input("Enter the price: ")),(input("Enter the quantity: "))])
    
    files = open("ProductList.txt", "w") 
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    