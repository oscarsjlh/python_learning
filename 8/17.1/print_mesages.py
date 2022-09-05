from modules_messages import *

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:],sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

