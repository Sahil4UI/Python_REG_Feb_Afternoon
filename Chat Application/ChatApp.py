#CHAT APPLICATION
chat = True

while chat:
    message = input("Enter message")
    message = message.lower()

    if (message == 'hello') or (message== 'hi') or (message == 'hey') or (message == 'hey there'):
        print("Hi")
    elif (message == 'bye'):
        print("Good Bye See you later......")
        chat = False

