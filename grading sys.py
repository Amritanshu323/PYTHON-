sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90 and avg<=100):
    print("Grade: M")
elif(avg>=60 and avg<=89):
    print("Grade: First")
elif(avg>=50 and avg<=59):
    print("Grade: Second")
elif(avg>=35 and avg<=49):
    print("Grade: 3rd")
elif(avg<35):
    print("Grade:4th")
else:
    print("Grade: Fail")
  
 
