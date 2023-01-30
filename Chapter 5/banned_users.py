banned_users = ['andrew', 'carolina', 'david']
user ='marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#The line at u reads quite clearly. If the value of user is not in the list
#banned_users, Python returns True and executes the indented line.

