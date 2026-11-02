import streamlit as st
import os

from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_pipeline import get_answer


# Configure the Streamlit page
st.set_page_config(
    page_title="AI Document Intelligence Assistant",
    page_icon="📚",
    layout="wide"
)

# Application heading
st.title("📚 AI Document Intelligence Assistant")
st.write("Upload PDF documents and ask questions about their content.")

# Create a folder for uploaded PDFs
UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload PDF documents
uploaded_files = st.file_uploader(
    "Upload your PDF documents",
    type=["pdf"],
    accept_multiple_files=True
)

# Process uploaded documents
if st.button("Process Documents"):

    if not uploaded_files:
        st.warning("Please upload at least one PDF.")
    else:
        all_documents = []

        with st.spinner("Reading and processing PDFs..."):

            for uploaded_file in uploaded_files:

                file_path = os.path.join(
                    UPLOAD_FOLDER,
                    uploaded_file.name
                )

                # Save the uploaded PDF
                with open(file_path, "wb") as file:
                    file.write(uploaded_file.getbuffer())

                # Load and split the PDF
                documents = load_pdf(file_path)
                chunks = split_documents(documents)

                all_documents.extend(chunks)

            # Create the vector database
            create_vector_store(all_documents)

            st.session_state["documents_processed"] = True

        st.success("Documents processed successfully!")

# Ask questions
if st.session_state.get("documents_processed", False):

    st.subheader("Ask Questions")

    question = st.text_input(
        "Enter your question about the uploaded documents:"
    )

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner("Searching documents and generating answer..."):

                answer, sources = get_answer(question)

            st.subheader("Answer")
            st.write(answer)

            st.subheader("Sources")

            for source in sources:
                st.write(f"📄 {source}")

        else:
            st.warning("Please enter a question.")