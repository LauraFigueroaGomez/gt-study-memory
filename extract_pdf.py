from pathlib import Path
import pymupdf

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


if __name__  == "__main__":
    pages = extract_pages(
        pdf_path,
        course_name
    )

    print(f"Total records: {len(pages)}")
    print(f"First page: {pages[0]['page']}")
    print(f"Last page: {pages[-1]['page']}")
    print(pages[0]["text"][:500])