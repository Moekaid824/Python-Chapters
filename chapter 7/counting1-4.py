current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

x = 1
while x <= 5:
    print(x)
    x += 1

# This loop runs forever!
x = 1
while x <= 5:
    print(x)
# Now the value of x will start at 1 but never change. As shown, the conditional test x <= 5 will always evaluate to True and the while loop will run forever, printing a series of 1s.
