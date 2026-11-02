from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()

# Connect to Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
    timeout=60
)

# Send a simple test message
response = llm.invoke("Explain supervised learning in two sentences.")

print("\nGemini Response:")
print(response.content)