n = int(input("enter numbers till u want to print: "))
operation = int(input("1.even\n2.odd\n3.natural\n"))

if operation == 1:
    for i in range(1,n+1):
        if i % 2 == 0:
            print('Even number :',i)
elif operation == 2:
    for i in range(1,n+1):
        if i %2 != 0:
            print('Odd numbers are :',i)
elif operation == 3:
    for i in range(1,n+1):
        print("the natural numbers are:",i)
else:
    print('Bhai kuch to gadbad ho gye hai')