#Program 4:To constructthe pattern:

rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print(" * ",end="")
    print("\n")
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print(" * ",end="")
    print("\n")
        
            


        
            
