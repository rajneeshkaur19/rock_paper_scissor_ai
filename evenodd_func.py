
n = int(input("enter the number till u wanna print:"))
user_input = int(input("which numbers u wanna print : 1.even\n 2.odd\n 3.natural\n"))

# if the number is even
def even():
    for i in range(1,n+1):
        if i%2==0:
            print("even numbers:",i)

# if the number is odd/function to print odd values            
def odd():
    for i in range(1,n+1):
        if i%2!=0:
            print("odd numbers:",i)


#function to print natural numbers            


def natural():
    for i in range(1,n+1):
            print("natural numbers:",i)


if user_input == 1:
     even()

elif user_input == 2:
     odd()     

elif user_input == 3:
     natural()


