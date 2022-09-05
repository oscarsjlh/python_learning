favorite_numbers = {
    'mandy': [10,20,30],
    'micah': [3,6,9,23],
    'gus': [6,66,666,6666],
    'hank': [1000000,10000294310942,19243254],
    'maggie': [0,1,2,3,4],
    }

for name, numbers in favorite_numbers.items():
    print(f"\nP{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\n{number}")
