

dream_vacations = {} 
polling_active = True

while polling_active:
    name = input("\nWhat's your name")
    message = 'Of you could visit one place in the world where would you go? '
    poll = input(message)

    dream_vacations[name] = poll

    repeat = input("Is there someone else to respond (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n----Poll Responses")

for name, dream_vacation in dream_vacations.items():
    print(f"{name} would like to go {dream_vacation}")
    
