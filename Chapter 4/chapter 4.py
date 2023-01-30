#index      0        1         2         3
foods = ["pizza", "tacos", "dim sum", "sushi"]
# listname[index]
print(foods[1])

#for PLACEHOLDER in THE_LIST_WE_WAnt_TO_LOOK_AT:
    # this is a code block (because of indentation)
    # this code block
    # will run in for every item in the list
for food in foods:
    print(food.title())
    print(type(food))
print("loop is over")

foods = ["pizza", "tacos", "dim sum", "sushi"]
for food in foods:
    print(
        f"I like to eat",food
        )
    print(type(food))
print("loop is over")
           #OR
for food in foods:
    print(f"I like to eat {food}",)
    print(type(food))
print("loop is over")

for food in foods:
    print(f"I like {food} because they are yummy")
    if food == "pizza":
        break   #(It'll only print pizza and break the others)

for food in foods:
    print(f"I like {food} because they are yummy")
    if food == "dim sum":
        break   #(It'll only print pizza, tacos and dim sum and break the others)


#for food in foods:
#    if food == "pizza":
#        break
#    print(f"I like {food} because they are yummy") ------------DON"T RUN IT LIKE THIS WILLNOT GET ANY OUTPUT

for food in foods:
    if food == "pizza":
        continue    #CONTINUE SKIPS PIZZA AND LISTS THE REST
    print(f"I like {food} because they are yummy")

for food in foods:
    if food == "dim sum":
        continue    #CONTINUE SKIPS DIM SUM AND LISTS THE REST
    print(f"I like {food} because they are yummy")

# my_list = [0,1,2,3]------created form range function
# for index in my_list:
for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))
for tup in enumerate(foods):
    print(tup)

print(list(enumerate(foods)))
for index, food in enumerate(foods):
    print(f"My No {index + 1}, food is {food.title()}")

# Loop of the index
print(list(range(4)))
print(len(foods))

# Food is a string
# Index is an integer