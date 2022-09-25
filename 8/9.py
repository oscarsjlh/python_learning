
def show_messages(unsent_messages, sent_messages):

    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending the message: {current_message}")
        sent_messages.append(current_message)
def show_sent(sent_messages):

    for sent_message in sent_messages:
        print(f"\n You have sent the following messages: {sent_message}")

messages_tosend= ['album','packet','hail sabath!']
sent_messages = []

show_messages(messages_tosend,sent_messages)
show_sent(sent_messages)
print(messages_tosend)
print(sent_messages)
