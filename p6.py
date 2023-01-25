import time
import random

def flipCoins(): 
    heads = 0
    for i in range(100):
        if random.random() < 0.5: 
            heads += 1 
    return heads

def main(): 
    print("Number of heads: " + str(flipCoins()) + " out of 100") 

main()