# 1. DEFINING THE FUNCTION USING "rule_based_chatbot"
def rule_based_chatbot():
    print("Bot: Greetings, Master! I am your precise assistant.")

    #DEFINING THE CONVERSATIONAL FLOW FUNCTION

    # We start at Stage 1: Waiting for a Greeting
    stage = 1

    while True:
        user_input = input("You: ").lower().strip()

        # INSTANT OVERRIDE: If the user wants to force quit at any time
        if "quit" in user_input:
            print("Bot: Farewell! May your journey be prosperous.")
            break

        # ==========================================
        # STAGE 1: THE GREETING (Only moves forward if you say hi)
        # ==========================================
        if stage == 1:
            if "hello" in user_input or "hi" in user_input or "hey" in user_input or "greeting" in user_input:
                print("Bot: Hello! It is an honor to meet you. Tell me, how fares your day today?")
                stage = 2  # Turn the page to Chapter 2!
            else:
                print("Bot: A proper conversation always begins with a greeting! so shall we greet each other first?.")

        # ==========================================
        # STAGE 2: THE MOOD CHECK (Only processes feelings here)
        # ==========================================
        elif stage == 2:
            if "not bad not good" in user_input or "neither" in user_input:
                print("Bot: Ah, a balanced or heavy heart. I hope your path clears up soon.")
                print("Bot: Type 'quit' when you are ready to end our conversation.")
                stage = 3  # Turn the page to Chapter 3!

            elif "not good" in user_input or "bad" in user_input or "sad" in user_input:
                print("Bot: I'm sorry to hear that. I hope your days become brighter!")
                print("Bot: Type 'quit' when you are ready to end our conversation.")
                stage = 3

            elif "okay" in user_input or "good" in user_input or "fine" in user_input:
                print("Bot: Splendid! It is good to see you in high spirits.")
                print("Bot: Type 'quit' when you are ready to end our conversation.")
                stage = 3

            else:
                print("Bot: Forgive me, I am checking your mood. Are you feeling 'good', 'bad', or 'neither'?")

        # ==========================================
        # STAGE 3: THE FAREWELL (Waiting for exit)
        # ==========================================
        elif stage == 3:
            if "bye" in user_input or "good bye" in user_input or "quit" in user_input or "tata" in user_input or "goodbye" in user_input:
                print("Bot: Farewell! May your journey be prosperous.")
                break
            else:
                print("Bot: Our formal conversation has concluded. Please say 'bye' or 'quit' to exit.")

# 2. RUNNING THE FUNCTION
rule_based_chatbot()
