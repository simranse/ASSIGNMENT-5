#Program to reverse the string:

n=input("Enter any string:")
reverse_string=""
count=len(n)
while count>0:
    reverse_string+=n[count-1]
    count=count-1
print("The reverse of the string is:",reverse_string)
