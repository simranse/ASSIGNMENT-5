#Program 6: To find prime numbers between the given range:

lower=int(input("Enter the lower value of range:"))
upper=int(input("Enter the upper value of range:"))
print("The prime numbers in the range are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
             print(num)
