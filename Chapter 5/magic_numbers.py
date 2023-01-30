answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)

print(age <=21)

print(age >21)

print(age >=21)
#To check whether two conditions are both True simultaneously, 
#use the keyword and to combine the two conditional tests; if each test passes,
#the overall expression evaluates to True. If either test fails or if both tests fail,
#the expression evaluates to False.
#For example, you can check whether two people are both over 21 using
#the following test:
age_0 = 22
age_1 = 18
print (age_0 >= 21 and age_1>= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
