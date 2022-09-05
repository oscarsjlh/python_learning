information = {
        'first_name': 'oscar',
        'last_name': 'aranega',
        'age' : '23',
        'city' : 'london',
        }

print(information['first_name'])
print(information['last_name'])
print(information['age'])
print(information['city'])



## Programing Values


favourite_statements = {
        'variables' : '\"Boxes to store Values\"\n',
        'string' : '\"data type that contains letters \"\n',
        'if' : '\"Statements that check if something is true\"\n',
        'list' : '\"variables that store multiple values\"\n',
        'for' : '\"they do something for every value\"\n',
         }
        
for name, statement in favourite_statements.items():
    print(f"{name.title()} do: {statement.title()}")
