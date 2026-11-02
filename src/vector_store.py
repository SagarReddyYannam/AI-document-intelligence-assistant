# Import Hugging Face embedding class
from langchain_huggingface import HuggingFaceEmbeddings

# Import Chroma vector database
from langchain_chroma import Chroma


# Create a function to build our vector database
def create_vector_store(chunks):

    # Load a free embedding model locally
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Define where ChromaDB will save its data
    persist_directory = "chroma_db"

    # Convert document chunks into embeddings
    # and store them in ChromaDB
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name="document_assistant"
    )

    # Return the created vector database
    return vector_store