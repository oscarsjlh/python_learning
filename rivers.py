rivers = {
        'nile': 'egipt',
        'thames':'united kingdom',
        'ebre': 'spain',
        }

for name, definition in rivers.items():
    print(f"The {name.title()} runs through {definition.title()}")

for name in rivers.keys():
    print(f"{name.title()}\n")
for name, definition in rivers.items():
    print(f"{definition.title()}\n")
