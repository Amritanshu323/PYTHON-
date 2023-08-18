s="NUN"
r=""
for i in s:
    r = i + r
l = len(s)
for i in range(1,l):
    if(s[i]!=r[i]):
         break
if(i==l-1):
   print("PALINDROME")
else:
   print("NOT PALINDROME")
    
