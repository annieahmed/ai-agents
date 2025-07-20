import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class ScamDetector:
    def analyze(self, message):
        prompt = f"Is the following message a scam or safe?\n\nMessage: {message}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=20
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"
