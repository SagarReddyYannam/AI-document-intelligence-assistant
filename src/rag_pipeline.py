# ==========================================
# AI DOCUMENT INTELLIGENCE ASSISTANT
# RAG PIPELINE
# ==========================================

# Import the required libraries
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# ==========================================
# STEP 1: LOAD EXISTING VECTOR DATABASE
# ==========================================

def get_vector_store():

    # Use the same embedding model used during indexing
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Connect to the existing ChromaDB database
    vector_store = Chroma(
        collection_name="document_assistant",
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return vector_store


# ==========================================
# STEP 2: GENERATE ANSWER USING RAG
# ==========================================

def get_answer(question):

    # Initialize the local Ollama language model
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.2
    )

    # Load the existing vector database
    vector_store = get_vector_store()

    # Retrieve the 3 most relevant document chunks
    relevant_docs = vector_store.similarity_search(
        question,
        k=3
    )

    # Check whether relevant documents were found
    if not relevant_docs:
        return (
            "The uploaded documents do not contain enough information "
            "to answer this question.",
            []
        )

    # Combine retrieved document text into one context
    context = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    # ==========================================
    # STEP 3: CREATE THE PROMPT
    # ==========================================

    prompt = f"""
    You are a helpful document assistant.

    Answer the question using ONLY the context provided below.

    Rules:
    1. Do not use outside knowledge.
    2. Do not make up information.
    3. If the answer is not available in the context,
       clearly say that the uploaded documents do not contain the answer.
    4. Give a clear and simple answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # ==========================================
    # STEP 4: GENERATE THE ANSWER
    # ==========================================

    response = llm.invoke(prompt)

    # Extract the answer text
    answer = response.content

    # ==========================================
    # STEP 5: COLLECT SOURCE INFORMATION
    # ==========================================

    sources = []

    for doc in relevant_docs:

        # Get the PDF filename
        source = doc.metadata.get("source", "Unknown")

        # Get the original PDF page number
        page = doc.metadata.get("page", "Unknown")

        # Convert zero-based page number to normal page number
        if isinstance(page, int):
            page = page + 1

        # Create source information
        source_info = f"{source} - Page {page}"

        # Avoid duplicate source entries
        if source_info not in sources:
            sources.append(source_info)

    # ==========================================
    # STEP 6: RETURN ANSWER AND SOURCES
    # ==========================================

    return answer, sources