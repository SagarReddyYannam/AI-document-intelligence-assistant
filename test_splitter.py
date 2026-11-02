# Import the PDF loader
from src.document_loader import load_pdf

# Import our text splitting function
from src.text_splitter import split_documents

# Load the PDF
documents = load_pdf("data/sample.pdf")

# Split the documents
chunks = split_documents(documents)

# Display the total number of chunks
print("Total chunks:", len(chunks))

# Display the first chunk
if chunks:
    print("\nFirst chunk content:")
    print(chunks[0].page_content)

    # Display its metadata
    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)