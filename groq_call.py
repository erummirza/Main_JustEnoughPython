
from dotenv import load_dotenv  # <--- Add this
from groq import Groq

load_dotenv()                   # <--- Add this


MODEL = "openai/gpt-oss-120b"
client = Groq()  # reads GROQ_API_KEY

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain tokens in one sentence."}]
)

print(resp.choices[0].message.content)
print(resp.usage.prompt_tokens, resp.usage.completion_tokens)