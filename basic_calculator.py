operation = int(input("Enter the operation u want to perform : \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Divison \n:"))
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter 2nd Number:"))

if operation == 1:
   print(num1+num2)

elif operation == 2:
   print(num1-num2)

elif operation == 3:
   print(num1*num2)
     
elif operation == 4:
   if(num2 == 0):
      print("cannot be divisible")
   else:
      print(num1/num2)     
