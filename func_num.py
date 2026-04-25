def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        num = int(input("what's n?:"))
        if num>0:
            break
    return num
    
def meow(num):
    for _ in range(num):
        print("meow")

main()
    
              