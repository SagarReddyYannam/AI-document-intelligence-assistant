# Import the PDF loading function
from src.document_loader import load_pdf

# Import the text splitting function
from src.text_splitter import split_documents

# Import our vector database function
from src.vector_store import create_vector_store


# STEP 1: Load the PDF document
documents = load_pdf("data/sample.pdf")

# STEP 2: Divide the PDF into smaller chunks
chunks = split_documents(documents)

print("Total chunks:", len(chunks))


# STEP 3: Convert chunks into embeddings
# and save them in ChromaDB
vector_store = create_vector_store(chunks)

print("Vector database created successfully!")


# STEP 4: Ask a question
query = "What is Machine Learning?"


# STEP 5: Retrieve the three most relevant chunks
results = vector_store.similarity_search(
    query,
    k=3
)


# STEP 6: Display retrieved information
print("\nRetrieved information:")

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}:")

    # Print the original document text
    print(result.page_content)

    # Print the source and page information
    print("Source:", result.metadata.get("source"))
    print("Page:", result.metadata.get("page"))