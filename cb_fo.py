import random

def get_response(user_input):
    responses = {
        "hello": "Hi there! Ready to order some delicious food?",
        "menu": "Would you like to see the menu?",
        "order": "What would you like to order today?",
        "bye": "Thank you for ordering! Enjoy your meal.",
        "default": "I'm not sure what you're asking. Can you order or check the menu?"
    }
    return responses.get(user_input.lower(), responses["default"])

def main():
    print("Food Ordering Chatbot")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Enjoy your meal.")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()



# 1)get_response
# user_input is the input provided by the user to the chatbot.
# The responses dictionary contains various keys (like "hello," "menu," "order," "bye," and "default"), each representing different user queries or interactions with the chatbot.
# The function converts the user_input to lowercase using user_input.lower() to ensure case insensitivity.
# responses.get(user_input.lower(), responses["default"]) is a dictionary method that looks for the user input in the responses dictionary. If the user input matches any key in the dictionary, it returns the corresponding value (the chatbot's response). If the user input doesn't match any keys, it returns the default response, which is set as "I'm not sure what you're asking. Can you order or check the menu?"

# 2)main()
# print("Food Ordering Chatbot") and print("Type 'bye' to exit.") display initial messages to inform users about the chatbot's purpose and how to exit the conversation.

# Inside the while True: loop, the program continuously prompts the user for input using user_input = input("You: ").

# If the user enters 'bye' (case insensitive), the chatbot responds with a farewell message ("Chatbot: Goodbye! Enjoy your meal.") and exits the loop using break.

# Otherwise, it calls the get_response() function, passing the user input as an argument. The returned response from get_response() is stored in the response variable.

# Finally, it prints the chatbot's response (f"Chatbot: {response}") to the user's input.


# 3)if __name__ == "__main__":

# __name__ is a special variable in Python. When a Python script runs, Python sets the __name__ variable based on how the script is executed:

# If the script is executed as the main program, Python sets __name__ to "__main__".
# If the script is imported as a module into another script, Python sets __name__ to the name of the module.
# if __name__ == "__main__": checks if the script is being run directly (i.e., as the main program). If __name__ is equal to "__main__", it means the script is being executed standalone and not imported as a module.

# When if __name__ == "__main__": evaluates to True, it executes the code block within it. In this case, it calls the main() function, initiating the execution of the food ordering chatbot.