import os

from groq import Groq
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(query, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are Titan, an academic AI assistant.

Answer the user's question ONLY using the provided context.
Answer clearly and completely in 4–6 lines.
Do not copy chunks.
Synthesize from context.
If the answer is not present in the context, say:
"I could not find that in the provided material."

QUESTION:
{query}

CONTEXT:
{context}
"""

    completion = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return completion.choices[0].message.content