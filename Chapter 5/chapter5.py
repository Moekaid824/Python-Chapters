# Boolean can be two things ON or Off True or False Yes or NO
My_bool = True
print(My_bool)
my_bool = False
print(my_bool)
#list() convert something to a list when talking about integir
#int() convert string to integer
#str() convert integer to string
#bool() convert something into a boolian
print(bool(0))
print(bool(1))
print(bool(-123)) #any number not zero will be true
print(bool(''))
print(bool('words')) #anything in it is true and nothing in it is false

# > < >= <= == != #greater than, less than, greather than or equal too,
#less than or equal too, equal too, not equal too

print("dog"=="dog")
print("dog"=="Dog")
print("dog"=="Dog".lower())
print(4 < 6)
print(4 > 6)
print(6 < 6)

x = 10
print(5 < x < 20)
x = 2
print(5 < x < 20)

letter="a"
print(letter>"b")
letter="c"
print(letter>"b")
letter="d"
print(letter>"b")
letter="a"
print(letter> "A")
letter="A"
print(letter>"B")
letter="A"
print(letter< "B")

letter="A"
print(ord("A"))
print(letter<"B")
letter="A"
print(ord("A"))
print(ord("B"))
print(letter<"B")
letter="A"
print(ord("a"))
print(ord("b"))
print(letter<"B")

x= 10
y = 10
z = 20
print(x == 10 and y ==10)
x= 10
y = 10
z = 20
print(x == 10 and z ==10)
x= 10
y = 10
z = 20
print(x == 10 and z ==10)
x= 10
y = 10
z = 20
print(x == 10 or z ==10) # if you have an OR and one is true you'll get a true
#if you have an AND one is false you'll get a false

x = 8
y = 9
print(x == y)
x = 8
y = 9
print(x != y)
x = 8
y = 9
print(not x == y)
x = 8
y = 9
print(not True)
x = 8
y = 9
print(not True or False)
x = 8
y = 9
print(not True and True)

#if BOOLEAN OR BOOLEAN EXP:
    #code block
    #for if true
#else:
    # for the if false code black

height = 55

#Must be 5 feet tall to ride my ride
#Must be under 6 feet tall to ride

if height < 60:
    print("You are too Short")
    print("I am sorry but get off my ride!")

    height = 65

if height < 60:
    print("You are too Short")
    print("I am sorry but get off my ride!")
elif height > 72:
    print("You are too tall!")
    print("get off my ride!")
#this won't do anything due to being less than the height

    height = 65

if height < 60:
    print("You are too Short")
    print("I am sorry but get off my ride!")
else:
    print("Enjoy the Ride!")
print("Thanks for visiting")

height = 75

if height < 60:
    print("You are too Short")
    print("I am sorry but get off my ride!")
elif height > 72:
    print("You are too tall!")
    print("get off my ride!")