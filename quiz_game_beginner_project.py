print("WELCOME TO MY COMPUTER QUIZ")

user = int(input("do you want to play the quiz?:\n 1. YES\n 2. NO\n"))
if user == 1:
    print("LET'S START THE QUIZ")

    answer = input("what does CPU stands for?").strip().lower()
    if answer == "central processing unit":
        print("correct")
    else:
        print("incorrect")   

    answer = input("what does GPU stands for?").strip().lower()
    if answer == "graphics processing unit":
        print("correct")
    else:
        print("incorrect")

    answer = input("what does RAM stands for?").strip().lower()
    if answer == "Random access memory":
        print("correct")
    else:
        print("incorrect")      

    answer = input("what does psu stands for?").strip().lower()
    if answer == "power supply":
        print("correct")
    else:
        print("incorrect")     

    answer = input("what does ROM stands for?").strip().lower()
    if answer == "Read only memory":
        print("correct")
    else:
        print("incorrect")  

        print("thank u for playing the quiz!!!!")   

elif user == 2:
    print("THE QUIZ IS OVER AS YOU DON'T WANNA PLAY")
else:
    print("you didn't select the correct option that is given above")        
