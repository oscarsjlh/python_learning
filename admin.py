users = [] 
if users:
    for user in users:
        if user == 'admin':
            print('Hello Admin would you like to see the report')
        else:
            print(f"Hello {user} thank you for login in again")
else:
    print("Please add some users")


current_users = ['admin', 'oscar', 'valentine', 'drAkonus', 'hArry']
new_users = ['marcone', 'legolas', 'harry']

lowercase_users = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user in lowercase_users:
        print(f"Sorry {new_user} please select a new username")

