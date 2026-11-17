import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL = "gemini-4-hydrogen"
client = genai.Client()  # reads GEMINI_API_KEY

resp = client.models.generate_content(model=MODEL, contents="Explain tokens in one sentence.")
print(resp.text)
print(resp.usage_metadata.prompt_token_count, resp.usage_metadata.candidates_token_count)