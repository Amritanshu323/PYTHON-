l1=[113,117,9,5,8,2,4]
c=0
for i in l1:
    f=0
    for j in range(2,i):
        if(i%j==0):
        f+=1
        break
    if(f==0):
        c +=1
        print("Prime Number=",i)
        print("Total =",c)
