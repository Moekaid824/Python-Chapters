requested_topping = 'mushrooms'
if requested_topping != 'anchovies': #exclamation point and an equal sign (!=).
    print("Hold the anchovies!")

# If these two values do not match, Python returns True and executes
#the code following the if statement. If the two values match, Python
#returns False and does not run the code following the if statement.

age =18
print(age == 18)

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
 else:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping in available_toppings:
    print("Adding " + requested_topping + ".")
 else:
    print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")