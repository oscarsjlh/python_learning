class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):

        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attemps = 0
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")
    def increment_login_attemps(self):
        self.login_attemps += 1 
    
    def reset_logins(self):
        self.login_attemps = 0

class Privileges(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []
    def show_privileges(self):
        print(f"User has the following privileges")
        for privlege in self.privileges:
            print(f"\n {privlege}")


oscar = Privileges('Oscar', 'Aranega', 'oas', 'oscar.aranega@gmail.com', 'london')
oscar.describe_user()
oscar.greet_user()
oscar.increment_login_attemps()
oscar.increment_login_attemps()
oscar.increment_login_attemps()

print(f"{oscar.username} has loged in {oscar.login_attemps}")
print(f"Clear log in attemps")
oscar.reset_logins()
print(f"{oscar.login_attemps}")


oscar.privileges = ['admin' , 'add user' , 'ban user']
oscar.show_privileges()
