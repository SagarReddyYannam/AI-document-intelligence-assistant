📚 AI Document Intelligence Assistant

An end-to-end Generative AI application that allows users to upload PDF documents and ask questions about their content. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and generate context-aware answers with source references.

🚀 Project Overview

Reading and searching through lengthy PDF documents can be time-consuming. This project simplifies that process by allowing users to upload PDF files and interact with their content using natural language questions.

The application retrieves relevant document chunks using semantic search and generates answers using a locally running Large Language Model (LLM).

✨ Features

- Multiple PDF Uploads: Upload multiple PDF documents.
- Document Processing: Extract and split PDF text into smaller chunks.
- Semantic Search: Retrieve relevant information based on the user's question.
- RAG Pipeline: Generate answers using retrieved document context.
- Source References: Display source document names and page numbers.
- Local LLM: Use Ollama with the Llama 3.2 model.
- Vector Database: Store and retrieve document embeddings using ChromaDB.
- Interactive Interface: User-friendly interface built with Streamlit.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming language
Streamlit| User interface
LangChain| RAG pipeline and integrations
Hugging Face| Text embedding model
Sentence Transformers| Generate text embeddings
ChromaDB| Vector database
Ollama| Run the local LLM
Llama 3.2 (3B)| Answer generation
PyPDF| Extract text from PDF files

🏗️ System Architecture

                 User
                   |
                   v
             Streamlit UI
                   |
                   v
              PDF Upload
                   |
                   v
             PDF Text Loader
                   |
                   v
              Text Splitting
                   |
                   v
          Hugging Face Embeddings
                   |
                   v
               ChromaDB
                   |
                   v
             User Question
                   |
                   v
          Semantic Similarity Search
                   |
                   v
           Relevant Document Chunks
                   |
                   v
              RAG Pipeline
                   |
                   v
             Ollama LLM
             (Llama 3.2)
                   |
                   v
          Answer + Source References

⚙️ Installation and Setup

1. Clone the Repository

git clone https://github.com/SagarReddyYannam/AI-document-intelligence-assistant.git

2. Navigate to the Project Folder

cd AI-document-intelligence-assistant

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

5. Install Dependencies

pip install -r requirements.txt

6. Install and Start Ollama

Download and install Ollama from:

https://ollama.com/

Download the Llama 3.2 model:

ollama pull llama3.2:3b

Make sure Ollama is running before starting the application.

7. Run the Application

python -m streamlit run app.py

Open the local URL displayed in your terminal, usually:

http://localhost:8501

📂 Project Structure

AI-document-intelligence-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
├── tests/
│
├── data/
│   └── uploads/
│
└── chroma_db/

Note: "data/" and "chroma_db/" are generated or used locally and are excluded from GitHub.

🔍 How It Works

1. The user uploads one or more PDF documents through the Streamlit interface.
2. PyPDF extracts the text from the uploaded documents.
3. LangChain text splitters divide the text into smaller chunks.
4. Hugging Face generates vector embeddings for the chunks.
5. ChromaDB stores the embeddings for efficient retrieval.
6. When the user asks a question, semantic similarity search retrieves relevant chunks.
7. The RAG pipeline sends the retrieved context and question to the Ollama LLM.
8. The LLM generates an answer based on the retrieved document context.
9. The application displays the answer along with source document and page references.

🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding Generative AI and Large Language Models (LLMs).
- Implementing Retrieval-Augmented Generation (RAG).
- Working with text embeddings and semantic search.
- Using vector databases for document retrieval.
- Integrating locally hosted LLMs using Ollama.
- Building interactive AI applications using Streamlit.
- Organizing Python projects into modular components.

🔮 Future Improvements

- Add conversational memory and chat history.
- Improve document management and deletion.
- Add support for additional document formats.
- Implement a FastAPI backend.
- Deploy the application to a cloud platform.
- Improve retrieval accuracy and answer evaluation.

👨‍💻 Author

Sagar Reddy Yannam

B.Tech Graduate | Aspiring AI Engineer | Machine Learning & Generative AI Enthusiast

GitHub: https://github.com/SagarReddyYannam

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.