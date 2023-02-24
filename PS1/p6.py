import time
import random

def main():
    print("Hello, welcome to Adam's Mind Reading Machine.")
    while True:
        try:
            state = str(input("Enter the current state: "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            a = int(input("Enter the amount of H -> H transitions for the first 21 flips (0-20): "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            b = int(input("Enter the amount of T -> T transitions for the first 21 flips (0-20):  "))
            break
        except:
            print("That is not a valid option!")

    steps = 9
    print("The last 10 flips: ")
    for i in range(steps+1): 
        print(state, end=", ")  
        r = random.random() 
        if state == "H":
            if r <= (a/20):
                nextstate = "H"
            else:
                nextstate = "T"
        elif state == "T":
            if r <= (b/20):
                nextstate = "T"
            else:
                nextstate = "H"
        state = nextstate

main()