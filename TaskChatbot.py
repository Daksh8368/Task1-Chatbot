def chatbot():
    # Predefined responses dictionary
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you?": "I'm an AI, so I don't have feelings, but I'm here to help you!",
        "what is your name?": "I am a chatbot created by CodSoft.",
        "bye": "Goodbye! Have a great day!",
        "help": "You can ask me about the weather, my name, or just say hello!"
    }
    
    # Start conversation loop
    while True:
        # Capture user input
        user_input = input("You: ").strip().lower()
        
        # Check for exit condition
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: I'm sorry, I don't understand that. Try asking something else.")
            
chatbot()