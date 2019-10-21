## Fizzbuzz
## Sebastien Church

## Boolean Variables
fizz = False
buzz = False

for x in range(1,101):
    if(x % 3) == 0:
        fizz = True
    if(x % 5) == 0:
        buzz = True

    if fizz == True and buzz == True:
        print("FizzBuzz")
        ## reset the variables
        fizz = False
        buzz = False
    elif fizz:
        print("Fizz")
        ## reset variable
        fizz = False
    elif buzz:
        print("Buzz")
        ## reset variable
        buzz = False
    else:
        print(x)
