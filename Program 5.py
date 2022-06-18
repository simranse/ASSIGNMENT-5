#Program 5:

n=int(input("Enter the number of rows:"))
val=65
for i in range(n):
    for j in range(i+1):
        ch=chr(val)
        print(ch,end="")
        if val==90:
            val=val-25
        else:
            val=val+1
    print()
          
