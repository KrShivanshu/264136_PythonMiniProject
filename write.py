def updateList(List, Dictionary): 
    L = List    
    d = Dictionary
    
    for keys in d.keys():
        if keys == "PHONE":
            L[0][2] = str(int(L[0][2])-d['PHONE'])
        elif keys == "LAPTOP":
            L[1][2] = str(int(L[1][2])-d['LAPTOP'])
        else:
            L[2][2] = str(int(L[2][2])-d['HDD'])
    print("\nRemaining Stock Products:")
    for i in L:
        print(i[0]+" - "+i[2])
        
        
    files = open("ProductList.txt", "w") 
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
