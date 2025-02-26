#while loop
#nested loop
i=10
while i>=0:
    if i==5:
        continue
    else:
        print(i)
        i=i-1
        
#typecasting
a=10
b=str(a)
print(type(b))

s="hello"
l=list(s)
print(l)
k="".join(l)
print(k)

for i in range(5):
    print(i,end="  ")
print("\nhello","hi","welcome",end=" ")