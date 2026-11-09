from pathlib import Path
import pymupdf
import json

pdf_path = "data/raw/HTS-Introduction.pdf"
course_name = "CS6601"

def extract_pages(pdf_path, course):
    records=[]
    document_name= Path(pdf_path).name

    with pymupdf.open(pdf_path) as document:
        for page_number, page in enumerate(document, start=1):
            record = {
                "course": course,
                "document": document_name,
                "page": page_number,
                "text": page.get_text(),
            }
            records.append(record)
    
    return records

def save_records(records, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)

def load_records(output_path):
    with open(output_path,'r', encoding="utf-8") as file:
        return json.load(file)

if __name__  == "__main__":
    pages = extract_pages(
        pdf_path,
        course_name
    )

    print(f"Total records: {len(pages)}")
    print(f"First page: {pages[0]['page']}")
    print(f"Last page: {pages[-1]['page']}")
    print(pages[0]["text"][:500])

    output_path = Path("data/processed") / f"{Path(pdf_path).stem}.json"
    save_records(pages, output_path)
    loaded_pages = load_records(output_path)

    assert len(loaded_pages) == 54
    assert loaded_pages[0]["page"] ==1
    assert loaded_pages[-1]["page"] == 54
    assert loaded_pages == pages

    print(f"Saved and reloaded: {output_path}")




