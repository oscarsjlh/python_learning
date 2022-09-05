numbers = list(range(1,10))
exception_numbers = list(range(1,4))
for number in numbers:
    if number in exception_numbers:
        if exception_numbers == 1:
            print("1st\n")
        elif exception_numbers == 2:
            print("2nd\n")
        elif exception_numbers == 3:
            print("3rd\n")
    else:
        print(f"{number}\n")
