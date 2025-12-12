from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class Agent:
    """Groq-powered agent using llama-3.3-70b-versatile."""

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_email(self, employee_name):
        prompt = f"Write a professional but friendly onboarding email to {employee_name}."

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful and concise assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.3
        )

        return response.choices[0].message.content

