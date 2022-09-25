class User:
    """Simple class to define a user"""
    def __init__(self, first_name, last_name, id, tag):
        """Initialize the user"""
        self.first_name = first_name
        self.last_name  = last_name
        self.id         = id
        self.tag        = tag
        self.loginattemps = 0
    def describe_user(self):
        "Descrine the user"
        print("\nUser info:")
        print(f"\n{self.first_name.title()} {self.last_name.title()}")
        print(f" -User id: {self.id} \n -User tag: {self.tag}")
    def greet_user(self):
        print(f"\nWelcome {self.first_name.title()} have a good time!")
    def increment_logins(self):
        self.loginattemps = self.loginattemps + 1
        return(self.loginattemps)
    def reset_logins(self):
        self.loginattemps = 0
        return(self.loginattemps)

class Admin(User):
    def __init__(self, first_name, last_name, id, tag):
        super().__init__(first_name, last_name, id, tag)
        self.privileges = [] 
    def show_privileges(self):
        print(f"\n{self.first_name.title()} has the following privileges:")
        for privilege in self.privileges:
            print(f" -{privilege}")

admin1 = Admin('oscar','aranega','2213','superadmin') 
admin1.describe_user()
admin1.greet_user()
admin1.privileges = ['can post', 'can edit','can ban']
admin1.show_privileges()
