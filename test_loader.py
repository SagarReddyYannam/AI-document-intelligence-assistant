# Import our PDF loading function
from src.document_loader import load_pdf

# Specify the PDF location
pdf_path = "data/sample.pdf"

# Load the PDF
documents = load_pdf(pdf_path)

# Display the total number of pages
print("Total pages:", len(documents))

# Display the first page
if documents:
    print("\nFirst page content:")
    print(documents[0].page_content)

    # Display its metadata
    print("\nPage metadata:")
    print(documents[0].metadata)