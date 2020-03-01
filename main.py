import time
import sys

try_again = True

while try_again:
    
    div_30 = 0
    div_5 = 0
    div_3 = 0
    div_2 = 0
    div_2_and_3 = 0
    div_none = 0

    lower = int(input("Enter lowest number: "))
    higher = int(input("Enter highest number: "))

    for x in range(lower, higher+1):
        if x % 30 == div_30:
            print(x , "Foo")
            div_30 += 1
        elif x % 5 == div_5:
            print(x , "Bar")
            div_5 += 1
        elif x % 3 == div_2_and_3 and x % 2 == div_2_and_3:
            print(x , "FizzBuzz")
            div_2_and_3 += 1
        elif x % 3 == div_3:
            print(x , "Fizz")
            div_3 += 1
        elif x % 2 == div_2:
            print(x , "Buzz")
            div_2 += 1
        else:
            print("Bazz")
            div_none += 1

    total = higher - lower

    print("Total numbers evaluated: " + str(total))
    print("Divisible by 30:",div_30)
    print("Divisible by 5:",div_5)
    print("Divisible by 2 and 3:",div_2_and_3)
    print("Divisible by 3:",div_3)
    print("Divisible by 2:",div_2)
    print("Divisible by nothing:",div_none)
    
    try_again = str(input("Would you like to try again? (y/n) "))
    
    if try_again == "y":
        continue
    else:
        print("The window will now close.")
        time.sleep(3)
        sys.exit()
        break
