cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())

    # conditional test At the heart of every if statement is an expression that 
    # can be evaluated as True or False and is called a conditional test

# In order to get a true, both variables have to be the same
# In order to get a false, both variables have to be either different or
# one upper and lowercase letter 

car = 'bmw'
car == 'bmw'    # True because both bmw values are the same
print(car == 'bmw')

car = 'audi'
car == 'bmw'    # False because audi and bmw values aren't the same
print(car == 'bmw')

car = 'Audi'
car == 'audi'   # False because Audi values aren't the same due to A being capitalizied
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi')    # True because lower() function doesn’t change the value that was originally stored in car (converted the value car to lowercase)

car = 'Audi'
print(car.lower() == 'audi')    # True because Audi was the value converted the to lowercase
print(car)