from src.rag_pipeline import get_answer

# Ask a question about the uploaded PDF
question = "What is supervised learning?"

# Get the answer and source references
answer, sources = get_answer(question)

# Display the answer
print("\nANSWER:")
print(answer)

# Display the document sources
print("\nSOURCES:")
for source in sources:
    print(source)