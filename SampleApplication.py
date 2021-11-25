import random
from time import sleep

while True:
    number = random.randint(0, 100)
    if number%2 == 0:
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")

    sleep(2)