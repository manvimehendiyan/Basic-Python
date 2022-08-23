import math

x=float(input("Enter x: "))
n=int(input("Enter n: "))
Sum=float(1)
fact=float(1)
for i in range(1,n):
    fact*=i
    Sum+=(math.pow(x,i)/fact)
print("Sum of series (1 + x + x^2/2! +...+ x^n/n!): ",Sum)
