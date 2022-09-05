age = ""
message = "Please enter your age: "
message += "\n enter quit to enter"

while age != 'quit':
    age = input(message)
    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age <= 12:
        print("The ticket is 10$")
    else:
       print("The ticket is 15$") 
   
