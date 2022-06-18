# Program 8:

a=int(input("Enter any value:"))
b=int(input("Enter any value:"))
c=int(input("Enter any value:"))
d=int(input("Enter any value:"))
e=int(input("Enter any value:"))
f=int(input("Enter any value:"))
g=int(input("Enter any value:"))
h=int(input("Enter any value:"))
i=int(input("Enter any value:"))
j=int(input("Enter any value:"))
l=[a,b,c,d,e,f,g,h,i,j]
#(a)positive numbers
print("positive numbers are")
for i in l:
    if i>0:
        print(i)
#(b) negative numbers
print("negative numbers are")
for j in l:
    if j<0:
        print(j)
#(c)odd numbers
print("The odd numbers are")
for k in l:
    if k%2!=0:
        print(k)
#(d)even numbers
print("The even numbers are")
for m in l:
    if m%2==0:
        print(m)
#(e)
for i in l:
    count=l.count(i)
    print("The numbers of times ",i ,"occurs in the list is",count)
        
