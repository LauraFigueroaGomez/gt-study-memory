from extract_pdf import load_records

def chunk_pages(records, chunk_size=500):
    chunks = []
    for record in records:
        text = record["text"]
        for chunk_number, start in enumerate(range(0, len(text), chunk_size), start=1):
            passage = text[start:start+chunk_size]
            chunks.append({
                "course": record["course"],
                "document": record["document"],
                "page": record["page"],
                "chunk_number": chunk_number,
                "text": passage,
            })
    
    return chunks


if __name__ == "__main__":
    records = load_records("data/processed/HTS-Introduction.json")
    chunks = chunk_pages(records, chunk_size=500)
    first = chunks[0]

    print(f"Total chunks: {len(chunks)}")
    print(first["course"], first["document"], first["page"], first["chunk_number"])
    print(first["text"])

