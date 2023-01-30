# Don't indent unnecessarily for print statement
# message = "Hello Python world!"
#    print(message)

# Not an error but rather a mistake to get this code below!
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!")
# not putting a colon will cause an error
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
    # print(magician)