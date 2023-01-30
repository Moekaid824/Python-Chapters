# After you run this input function, The program waits while the user enters-
# their response in the terminal and continues after the user presses enter. The response is stored in the variable message, then print(message) displays the input back to the user.


name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

#