from groq import Groq
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    client = Groq(api_key=api_key)
else:
    raise ValueError("API key is not set. Check your .env file or environment variables.")
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role" : "system", "content": "You are a Financial assistant and you analyze the customers loan documentation, extract KPI's from it and anlyze the risk of acceptance accordingly. and finally give a score out of 10 to consider giving loan or no"},
        {"role" : "user", "content": "Do the latest available tesla earnings statement ?"}

    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
