#range
#functionname()
#.methodname()
#nested for loop for-if
a="chennai"
for i in range(len(a)):
    if (a[i])== "n":
        continue
else:
    print(a[i])
    
#for else
for i in range(1,10):
    if i==11:
        print(i)
        break
else:
    print("11 is not present in range")
    
#nested for loop
for i in range(1,5):
    for j in range(1,5):
        print(j)

#step index concept
for i in range(10,0,-1):
    print(i)