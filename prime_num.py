def prime_no(a,b):
    count=0
    print("\nPrime numbers between ",a," and ",b," are: ")
    for x in range(a+1,b):
        for i in range(2,x):
            if(x%i==0):
                break
        else:
            print(x)
            count+=1
    print("\nCount of prime numbers: ",count)
    
print("Enter 2 numbers: ")
a=int(input())
b=int(input())
prime_no(a,b)
