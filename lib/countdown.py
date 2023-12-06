
import time

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
    print("HAPPY NEW YEAR!")



def countdown_with_sleep(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        time.sleep(1)
        number -= 1
    print("HAPPY NEW YEAR!")

countdown_with_sleep(5)
    
    
