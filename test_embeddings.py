# Load environment variables from .env
from dotenv import load_dotenv

# Import the OpenAI embedding model
from langchain_openai import OpenAIEmbeddings

# Load the API key
load_dotenv()

# Initialize the embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Convert a sentence into a numerical vector
vector = embeddings.embed_query(
    "Machine Learning is a branch of Artificial Intelligence"
)

# Display the result
print("Embedding created successfully!")

# Display the number of dimensions
print("Vector dimensions:", len(vector))

# Display the first five vector values
print("First five values:", vector[:5])