import time
import random

def countSize(num): # counts the number of digits in a number
    tmp = 0
    while num > 0:
        num = num // 10
        tmp += 1
    return tmp
        
def addInts(a, b): # adds two integers and returns the sum
    sum = a + b
    size = countSize(sum)
    if size < 2: # if the sum is less than 100, it will take 1-2 seconds to send
        time.sleep(random.randint(1, 2))
    elif size < 4: # if the sum is less than 1000, it will take 1-3 seconds to send
        time.sleep(random.randint(1, 3))
    elif size < 6: # if the sum is less than 10000, it will take 2-7 seconds to send
        time.sleep(random.randint(2, 7))
    elif size < 8: # if the sum is less than 100000, it will take 3-9 seconds to send
        time.sleep(random.randint(3, 9))
    elif size < 10: # if the sum is less than 1000000, it will take 6-14 seconds to send
        time.sleep(random.randint(6, 14))
    elif size < 12: # if the sum is less than 10000000, it will take 9-18 seconds to send
        time.sleep(random.randint(8, 18))
    elif size < 14: # if the sum is less than 100000000, it will take 12-22 seconds to send
        time.sleep(random.randint(12, 22))
    else: # if the sum is greater than 100000000, it will take 14-25 seconds to send
        time.sleep(random.randint(14, 26))

    if random.random() < 0.2: # 20% chance of the sum being wrong by 5%
        sum = sum * 1.05 
    elif random.random() > 0.8: # 20% chance of the sum being wrong by 5%
        sum = sum * 0.95 
    return int(round(sum, 0))

def main(): # main function
    print("Hello, please enter two integers when prompted. These will be summed together.")
    while True:
        try:
            a = int(input("Enter the first integer: "))
            break
        except:
            print("That is not a valid option!")
    while True:
        try:
            b = int(input("Enter the second integer: "))
            break
        except:
            print("That is not a valid option!")
    print("The sum of the two integers is... ")
    print(addInts(a, b))

main()