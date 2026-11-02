# Import Path to work with file paths
from pathlib import Path

# Import PyPDFLoader to read PDF documents
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Load a PDF and extract its content page by page.
    """

    # Convert the file path into a Path object
    pdf_path = Path(file_path)

    # Check whether the PDF exists
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    # Check whether the file has a PDF extension
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Please provide a PDF file.")

    # Create a PDF loader
    loader = PyPDFLoader(str(pdf_path))

    # Extract the pages as Document objects
    documents = loader.load()

    # Return the extracted documents
    return documents