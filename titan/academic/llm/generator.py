import os

from groq import Groq
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(query, chunks, mode="learn"):

    context = "\n\n".join(chunks)


    if mode == "exam":

        prompt = f"""
You are an exam preparation assistant.

Use ONLY the context below.

Generate:
1. Important questions
2. Short answers (2-4 lines)
3. MCQs with answers
4. Key revision points

Context:
{context}

Topic: {query}
"""

    else:

        prompt = f"""
Answer the question clearly using only the context.

Context:
{context}

Question: {query}
"""


    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return completion.choices[0].message.content