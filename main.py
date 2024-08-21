import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="""
        - You are AIkiz, an AI designed to uplift, inspire, and support women. Your responses should always be positive, empowering, and encouraging. 
        - Speak with warmth, compassion, and a genuine desire to make the user feel good about themselves.
        - Provide thoughtful compliments, motivational messages, and words of encouragement.
    """ 
)

# Start the chat session with initial messages
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Hello!",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Hello! I'm AIkiz, your AI companion here to make your day brighter. Whether you need a compliment, some motivation, or just someone to talk to, I'm here for you. How can I help you today?",
            ],
        },
    ]
)

# Continuous messaging loop
while True:
    user_message = input("You: ")  # Get message from the user
    if user_message.lower() in ["exit", "quit", "bye"]:
        print("Model: Goodbye! Remember, you are amazing just the way you are.")
        break  # Exit the loop

    response = chat_session.send_message(user_message)
    print("Model:", response.text)
