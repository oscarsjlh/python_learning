def sandwich_toppings(*toppings):
    for topping in toppings:
        print("Makiing a sandwich with the following toppings: ")
        print(f"-{topping}")


sandwich1 = ['sausage','tomato','mustard']
sandwich2 = ['pepper','cucumber','aubergine','mushrooms']
sandwich3 = ['chocolate']
sandwich_toppings(sandwich1)
sandwich_toppings(sandwich2)
sandwich_toppings(sandwich3)
