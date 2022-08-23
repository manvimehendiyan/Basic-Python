D={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
print("Given dictionary D: ",D)

D[6]="Six"
print("\nNew Entry added in D: ",D)

D.pop(2)
print("\n2 removed from D: ",D)

if 6 in D:
    print("\nYes, 6 is present in D")
x=0    
for i in D:
    x+=1
print("\nNumber of elements in D is",x)

Sum=""
for i in D.values():
    Sum+=i
print("\nAddition of all values in D: ",Sum)

add=0
for i in D.keys():
    add+=i
print("\nAddition of all keys in D: ",add)
