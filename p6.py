import time
import random

def main():
    print("Hello, please enter the start state, the probability of H|H, and the probability of T|T.")
    while True:
        try:
            state = str(input("Enter the start state: "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            a = float(input("Enter the probability of H|H: "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            b = float(input("Enter the probability of T|T: "))
            break
        except:
            print("That is not a valid option!")

    steps = 31
    for i in range(steps+1): 
        print(state, end=", ")  
        r = random.random() 
        if state == "H":
            if r <= a:
                nextstate = "H"
            else:
                nextstate = "T"
        elif state == "T":
            if r <= b:
                nextstate = "T"
            else:
                nextstate = "H"
        state = nextstate

main()