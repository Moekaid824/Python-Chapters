prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
# This code works well, except that it prints the word 'quit' as if it
# were an actual message. A simple if test fixes this:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
     message = input(prompt)
     if message != 'quit':
          print(message)

# Now the program makes a quick check before displaying the message
# and only prints the message if it does not match the quit value:

# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# We set the variable active to True so the program starts in an active state. 
# Doing so makes the while statement simpler because no comparison is-
# made in the while statement itself; the logic is taken care of in other parts of the program.
# As long as the active variable remains True, the loop will continue running because of line 24.
