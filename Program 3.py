#Program 3:

a=float(input("Enter first side of the triangle:"))
b=float(input("Enter second side of the triangle:"))
c=float(input("Enter third side of the triangle:"))
if a+b>c and b+c>a and c+a>b:
    print("Combination of sides is possible!")
    s=a+b+c/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("The area of triangle is:",area)
else:
    print("Combination of sides is not possible!")
