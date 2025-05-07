n=int(input("Enter the no. of elements: "))
list=[]
for i in range(0 , n):
   x= int(input("Enter elements in list:"))
   list.append(x)
a=int(input("Enter the Element to found:"))
for i in range(n):
    if(list[i]==a):
        print("found", i)
        break
else:
    print("not found")
