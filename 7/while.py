current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something and I will repeat back to you: "
prompt += "\n Enter quit to end the program"

message = ""

while message != 'quit':
    message =input(prompt)
    print(message)
