# your code goes here!
import time
def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    return "HAPPY NEW YEAR!"

# print(countdown(10))
def countdown_with_sleep(number):
    # time.sleep(number)
    while number > 0:
        time.sleep(number)
        print(f'{number} SECOND(S)!')
        # time.sleep(number)
        number -= 1
    return "HAPPY NEW YEAR!" 
# print(countdown_with_sleep(5))