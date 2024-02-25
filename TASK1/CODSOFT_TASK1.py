# 1.Importing module-Regular Expression
import re

# 2.Matching responses from user
def simple_chatbot(user):
    # 2.1 Convert input from user to lowercase 
    user_inp = user.lower()

    # 2.2 Define some predefined rules and responses using Pattern Matching
    greetings = ['hi', 'hello', 'hey', 'hola']
    questions_patterns = ['how are you', 'how was your day']
    name_patterns = ['what is your name']
    goodbye_patterns = ['bye', 'adios']
    thanks_patterns = ['thank you', 'thanks', 'thx']

    # 2.3 Check user input against the rules using if-else statements
    if any(greeting in user for greeting in greetings):
        return 'Hello! How may I help you?'

    elif any(pattern in user for pattern in questions_patterns):
        return 'I\'m doing good. My day was great. Thank you for asking!'

    elif any(pattern in user for pattern in name_patterns):
        return 'My name is Maya. I\'m an AI based Chatbot.'

    elif any(pattern in user for pattern in goodbye_patterns):
        return 'Goodbye! Have a good day!'

    elif any(pattern in user for pattern in thanks_patterns):
        return 'You\'re Welcome!'

    else:
        return 'I\'m sorry, I didn\'t understand that. Can you please ask another question?'

# 3. Simple interaction loop
print("Chatbot: Hola! I'm an AI based chatbot. Type 'quit' to exit.")
while True:
    user_inp = input("User: ")
    
    if user_inp.lower() == 'quit':
        print("Goodbye!")
        break
    
    response = simple_chatbot(user_inp)
    print("Chatbot: ", response)


