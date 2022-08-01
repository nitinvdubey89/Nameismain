#import getpass

#users = [(0,'Bob','Mechanic'), (1,'kumar','Mechanic'), (2,'haitham','PS5'),(3,'salvatore','PS')]

#users_mapping = {user[1]: user for user in users}
#print(users_mapping["Bob"])

#for user in users:
#    if user[1] == "Bob":
#        print(user)

#username_input = input("Enter your username")
#password_input = getpass.getpass(prompt='Enter your pass ')

#_ , username,password = users_mapping[username_input]

#if password_input == password:
 #   print("your details are correct")
#else:
  #  print("Your details are incorrect")


import getpass

p = getpass.getpass(prompt='Your favorite flower? ')

if p.lower() == 'rose':
    print('Welcome..!!!')
else:
    print('The answer entered by you is incorrect..!!!')