#program 2:
lower=int(input("Enter the lower value of range:"))
upper=int(input("Enter the upper value of range:"))
num=int(input("Enter the number to be divisible by:"))
for i in range(lower,upper+1):
    if (i%num==0):
        print(i)
    
