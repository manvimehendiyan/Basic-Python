def common(l1,l2):
    found=0
    for x in l1:
        for j in l2:
            if x==j:
                print(x)
                found=1
    if found==0:
        print("\nNo common element")

list1=["apple","banana","cherry","mango","pinapple","guava"]
list2=["papaya","cherry","orange","apple","guava","watermelon"]
print("List 1: ",list1)
print("List 2: ",list2)
print("\nCommon elements from the lists are: ")
common(list1,list2)