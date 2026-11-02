# Import the recursive text splitter from LangChain
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    # Create a text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Split the documents into smaller chunks
    chunks = text_splitter.split_documents(documents)

    # Return the chunks
    return chunks