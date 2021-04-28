def updateList(List, Dictionary): 
    L = List    
    d = Dictionary
    
    for keys in d.keys():
        for l in L:
            if keys == str(l[0]).upper():
                l[2] = str(int(l[2])-d[keys])
    
    print("\nRemaining Stock Products:")
    for i in L:
        print(i[0]+" - "+i[2])
        
        
    files = open("ProductList.txt", "w") 
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
