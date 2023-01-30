age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#Often, you’ll need to test more than two possible situations, and to evaluate
#these you can use Python’s if-elif-else syntax. Python executes only one
#block in an if-elif-else chain. It runs each conditional test in order until
#one passes. When a test passes, the code following that test is executed and
#Python skips the rest of the tests.