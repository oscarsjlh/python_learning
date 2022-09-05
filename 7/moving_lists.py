#Start with a list of users that need to be verified
unconfirmed_users = ['oscar','valentine','harry']
#list that will contain the authenticated users has to be empty so we can add users to it.
confirmed_users = []

#verify each user until there are no more confirmed users.
#Move each verified user to the confirmed users list.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all verified users

print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Filling a dictionary with user input.

#Start with empty dictionary
responses = {}

# Set a flag to indicate polling is active.

polling_active = True

while polling_active:
    name = input("\nWhat is your name ")
    response = input("Which mountain would you like to climb someday? ")

#store response in dictionary
    responses[name] = response
#see if more people take the polling

    repeat = input("Would you like to let another person respond (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Poll is complete. Show the results
print("\n ---Pool Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
