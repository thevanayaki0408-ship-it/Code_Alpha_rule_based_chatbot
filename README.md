# Code_Alpha_rule_based_chatbot
      Code Alpha - Python Programming Internship - Task 4: Rule Based Chatbot 

# CodeAlpha: Basic simple Chatbot (Precise Rule-Based Assistant)

## **Project Overview**
        This project is a precise, rule-based chatbot developed as part of the Python Programming Internship at CodeAlpha. The assistant uses specific conversation stages and ordered logical execution to guide users smoothly through a natural, scripted interaction.

## **Key Concepts Used**
1. **Functions (`def`):** Modular code structure to wrap the main chatbot logic.
2. **State Management (`stage`):** Enforces a true "Order of Execution" so the bot responds accurately based on the conversation's context.
3. **String Manipulation (`.lower().strip()`):** Cleans up user inputs to avoid errors from accidental spaces or casing.
4. **Control Flow Loops (`while True`, `if-elif-else`):** Keeps the conversation active until an explicit exit command is issued.

## **Conversational Flow Chart**
1. **Stage 1 (The Greeting):** The bot welcomes the user and expects a standard greeting.
2. **Stage 2 (The Mood Check):** The bot dynamically analyzes positive, mixed, or negative responses (correctly parsing complex phrasing like "not bad").
3. **Stage 3 (The Farewell):** Concludes the conversation and waits for the exit keyword.

## **How to Run**
1. Copy the code from `rule-based chatbot.py`.
2. Paste it into any Python 3 environment (like OnlineGDB or Google Colab).
3. Hit **Run** and chat with the bot in the terminal!
