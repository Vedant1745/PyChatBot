import google.generativeai as ai
import pyttsx3  # Text-to-Speech engine

API_KEY = 'API KEY'

# Initialize the chatbot API
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("model-name")
chat = model.start_chat()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop for chatbot interaction
while True:
    # User inputs a query by typing
    user_input = input("You: ")

    if user_input.lower() == 'bye':  # Exit condition if 'bye' is typed
        speak("Goodbye!")
        print("Chatbot: Goodbye!")
        break

    # Send the user input (typed) to the chatbot and get a response
    response = chat.send_message(user_input)

    # Output the chatbot's response as text and speak it (Text-to-Speech)
    print('Chatbot:', response.text)
    speak(response.text)

