message = "Please tell me a number "
number = input(message)
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is divisble by 10")
else:
    print(f"\n The number {number} isn't divisble by 10")
