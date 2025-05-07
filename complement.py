n=int(input("Enter a number"))
a=bin(n)
l=[]
str
str(a)
b=len(a)
print(b)

for i in a[2:]:
    '''print(i)'''
    if(i=='0'):
        i='1'
        l.append(i)
    if(i=='1'):
        i='0'
        l.append(i)
print(l)        
