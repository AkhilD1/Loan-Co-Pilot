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
        {"role" : "system", "content": "You are my educational mentor and a python-programming teacher for a middle school. So frame your answers accordingly."},
        {"role" : "user", "content": "What are decorators?"}

    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
