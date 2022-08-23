import random

def odd_no(list1):
    count=0
    print("Odd numbers in the list are: ")
    for x in list1:
        if x%2!=0:
            count+=1
            print(x)
    print("Count of odd numbers: ",count,"\n")

def even_no(list1):
    count=0
    print("Even numbers in the list are: ")
    for x in list1:
        if x%2==0:
            count+=1
            print(x)
    print("Count of even numbers: ",count,"\n")
    
def prime_no(list1):
    count=0
    print("Prime numbers in the list are: ")
    for x in list1:
        for i in range(2,x):
            if(x%i==0):
                break
        else:
            print(x)
            count+=1
    print("Count of prime numbers: ",count,"\n")
    
L=random.sample(range(100,900),100)
odd_no(L)
even_no(L)
prime_no(L)
