from src.rag_pipeline import get_vector_store

# Load the existing vector database
vector_store = get_vector_store()

# Search for relevant PDF content
question = "What is supervised learning?"

results = vector_store.similarity_search(question, k=3)

# Display retrieved content
for i, doc in enumerate(results, start=1):

    print(f"\nRESULT {i}")
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)