import os
from titan.academic.ingestion.pdf_reader import extract_text_from_pdf
from titan.academic.processing.chunker import chunk_text
from titan.academic.embeddings.embedder import create_embeddings
from titan.academic.retrieval.search import semantic_search
from titan.academic.llm.generator import generate_answer


PDF_FOLDER = r"titan/data/pdfs"

all_chunks = []

print("Loading PDFs...")

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        path = os.path.join(PDF_FOLDER, file)

        print(f"Reading: {file}")

        text = extract_text_from_pdf(path)

        chunks = chunk_text(text)

        all_chunks.extend(chunks)


print("Creating embeddings...")

embeddings = create_embeddings(all_chunks)

print("Titan Academic Ready.\n")


while True:

    query = input("Ask Titan: ")

    if query.lower() == "exit":
        break

    results = semantic_search(
        query,
        all_chunks,
        embeddings
    )

    retrieved_chunks = [
        r["text"] for r in results
    ]

    answer = generate_answer(query, retrieved_chunks)

    print("\nTitan:\n")
    print(answer)
    print("\n")