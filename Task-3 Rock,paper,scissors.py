import random
def game():
    x=["Rock","Paper","Scissors"]
    computer=random.choice(x)
    user=input("Enter an option(--Rock--Paper--Scissors--):")
    print("\nUser choice:",user)
    print("computer choice:",computer)
    if user==computer:
        print("Both won!")
    elif user=="Rock" :
        if computer=="Paper":
            print("User wins")
        elif computer=="Scissors":
            print("User wins")
    elif user=="Paper":
        if computer=="Rock":
            print("Computer wins")
        elif computer=="Scissors":
            print("computer wins")
    elif user=="Scissors":
        if computer=="Rock":
            print("computer wins")
        elif computer=="Paper":
            print("user wins")
def main():
    print("\n=========-------------Welcome to the game-------------=========\n")
    while True:
        game()
        choice=input("If you want to continue type=yes in not type=no:\n")
        if choice.lower()!="yes":
            break
    print("\n**********Thanks for playing***********")

if __name__=="__main__":
    main()