#CHAT APPLICATION
chat = True
from datetime import datetime
import webbrowser

helloIntent = ['hello','hi','hey','hey there','wassup buddy']

while chat:
    message = input("Enter message")
    message = message.lower()

    if message in helloIntent:
        print("Hi")
    elif message == "date":
        date = datetime.now().date()
        print(date.strftime("%d/%m/%y"))
    elif message == "google.com":
        webbrowser.open(message)
        
    elif (message == 'bye'):
        print("Good Bye See you later......")
        chat = False
        

