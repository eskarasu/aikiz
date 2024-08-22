from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Generative AI model setup
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_message = request.form["message"]
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [user_message],
                },
            ]
        )
        response = chat_session.send_message(user_message)
        return render_template("index.html", user_message=user_message, bot_response=response.text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
