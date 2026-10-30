# 01. Take two numbers and display there,
#     .Addition, .Substraction, .Multiplication, .Modulus, .Exponentiation

#Addition
a=10
b=20
c=10+ 20
print('add =',c)

#Substraction
a=20
b=10
v=20-10
print("sub = ",v)

#Multiplication
a=6
b=3
s=6*3
print("Mul = ",s)

#Division
a=20
b=10
m=20/10
print("Div = ",m)

#Floor Divison
a=20
b=10
n=20//10
print("Floor = ",n)

#Modulus
a=20
b=10
k=20%10
print("Mod = ",k)

#Exponentation
a=2
b=3
c=a**3

print("Exp = ",c)

#Q2. Predict the output:
a=17
b=5

print(a / b)  # output=3.4
print(a // b) # output=3
print(a % b)  # output=2
print(a ** 2) # output=289

#Explain the Difference between :
  #1. "/" : It divides the first number by second number. and the output will be in 'integer' or 'float' format. 
  #2.  "//": These operator is called 'floor division' which divides first value by second and returns floor value(always Integer value)
  #3. "%": These is Modulus operator which divides the first value by second and always returns tthe remainder.
  #4. "**" : These operator is called as exponent, It multiplies a number by itself as many times as specified by the power.


# Q3. WAP to calculate the total price of a purchase.
# Given:
# Product price = 250
# Quantity = 4
# Calculate and print the total amount

Product_price = 250
Quantity = 4
Total_amount = Product_price * Quantity
print("Total Amount:",Total_amount)

#Q4. Write a program to calculate the average of three numbers.
     #Use the values 75, 80, and 95.

a=75
b=80
c=95
Avg = (75+80+95)/3
print("Avg:",Avg)    #output=83.33333...