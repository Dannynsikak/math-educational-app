from openai import OpenAI
from dotenv import load_dotenv
import os
import random

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_similar_questions(original_question):
    # Extract numbers from the original question
    numbers = [random.randint(1, 50) for _ in range(2)]

    # ensure AI understands the structure
    prompt = f"""
    Generate a new math problem that follows the same structure as:
    "{original_question}"
    Use different numbers but keep the solving method the same
    """
    response = OpenAI.chatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    new_question = response['choices'][0]['message']['content']

    # Example: get answer (modify based on your AI's response format)

    answer = eval(new_question.split("=")[1]) # ensure a proper parsing

    return new_question, answer