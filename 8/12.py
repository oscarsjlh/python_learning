def sandwich_toppings(*toppings):
    print("\nPreparing a sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

sandwich_toppings('peppers','tomato','lettuce')
sandwich_toppings('sausage','bacon')
sandwich_toppings('squash','tomato','hummus','lettuce')
