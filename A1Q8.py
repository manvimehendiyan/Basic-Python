L=[10,20,30,40,50,60,70,80]
print("Given List L: ",L)

L.append(200)
L.append(300)
print("\n200 and 300 added to L: ",L)

L.remove(10)
L.remove(30)
print("\n10 and 30 removed from L: ",L)

L.sort()
print("\nList sorted in asc order: ",L)

L.sort(reverse=True)
print("\nList sorted in desc order: ",L)