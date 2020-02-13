import time
import sys

div_30 = 0
div_5 = 0
div_3 = 0
div_2 = 0
div_2_and_3 = 0
div_none = 0

try_again = True

while try_again:

    lower = int(input("Enter lowest number: "))
    higher = int(input("Enter highest number: "))

    for x in range(lower, higher+1):
        if x % 30 == div_30:
            print(x , "Foo")
        elif x % 5 == div_5:
            print(x , "Bar")
        elif x % 3 == div_2_and_3 and x % 2 == div_2_and_3:
            print(x , "FizzBuzz")
        elif x % 3 == div_3:
            print(x , "Fizz")
        elif x % 2 == div_2:
            print(x , "Buzz")
        else:
            print("Bazz")

    total = higher - lower

    print("The total numbers evaluated was " + total + " .")
    print("There were " , div_30 , " numbers that are divisible by 30.")

try_again = str(input("Would you like to try again? (y/n) "))

if try_again == "y":
    continue
else:
    print("The window will now close.")
    time.sleep(3)
    sys.exit()
    break
