#Program 9

str=input("Enter any string:")
str=str.split()
i=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"occurs",count,"times in the list")
    i=i+1
