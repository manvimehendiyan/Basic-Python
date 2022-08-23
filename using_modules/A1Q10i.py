def interest(P,R,T):
    return (P*R*T)/100

amount=int(input("Enter the Principal Amount: "))
rate=int(input("Enter the Interest Rate(in percentage): ")) 
time=int(input("Enter the time(in years): "))

print("The compound interest is ",interest(amount,rate,time))