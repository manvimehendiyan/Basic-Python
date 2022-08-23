def leapyear(a,b):
    print("\nLeap years between ",a," and ",b," are: ")
    for x in range(a+1,b):
        if((x%4==0 and x%100!=0) or (x%400==0)):
            print(x)
    
print("Enter 2 years: ")
year1=int(input())
year2=int(input())
leapyear(year1,year2)
