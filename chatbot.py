# Simple Chatbot

def chatbot():
    print("Welcome to our chatbot! How can I assist you today?")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How can I assist you today?")
        elif user_input == "how are you":
            print("Bot: I'm doing well, thanks! How about you?")
        elif user_input == "what is your name":
            print("Bot: My name is Chatty, nice to meet you!")
        elif user_input == "quit" or user_input == "exit":
            print("Bot: It was nice chatting with you. Goodbye!")
            break
        elif "help" in user_input:
            print("Bot: I can assist you with general queries. Feel free to ask me anything!")
        elif "time" in user_input:
            import datetime
            now = datetime.datetime.now()
            print(f"Bot: The current time is {now.strftime('%H:%M:%S')}.")
        elif "date" in user_input:
            import datetime
            now = datetime.datetime.now()
            print(f"Bot: Today's date is {now.strftime('%Y-%m-%d')}.")
        elif "joke" in user_input:
            print("Bot: Why don't scientists trust atoms? Because they make up everything!")
        elif "weather" in user_input:
            print(
                "Bot: I'm not capable of providing real-time weather information, but I can suggest checking a weather website or app for the latest updates!")
        else:
            print("Bot: Sorry, I didn't understand that. Can you please rephrase your query?")


if __name__ == "__main__":
    chatbot()