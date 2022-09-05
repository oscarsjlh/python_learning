active = True
toppings =""
message = "PLease choose the pizza toppings: "
message += "\nUse quit when done "
while active:
    toppings = input(message)
    if toppings == "quit":
        active = False
    else:
        print(f"Adding {toppings} Ito the pizza")
