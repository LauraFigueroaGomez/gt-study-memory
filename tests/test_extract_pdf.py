import pymupdf

from extract_pdf import extract_pages, load_records, save_records


def test_extract_pages_preserves_text_and_blank_pages(tmp_path):
    pdf_path = tmp_path / "sample.pdf"

    with pymupdf.open() as document:
        page = document.new_page()
        page.insert_text((72, 72), "Hello study memory")
        document.new_page()  # A blank second page
        document.save(str(pdf_path))

    records = extract_pages(pdf_path, "TEST")

    assert len(records) == 2
    assert [record["page"] for record in records] == [1, 2]
    assert all(record["course"] == "TEST" for record in records)
    assert all(record["document"] == "sample.pdf" for record in records)
    assert records[0]["text"].strip() == "Hello study memory"
    assert records[1]["text"].strip() == ""
    

def test_save_and_load_round_trip(tmp_path):
    pdf_path = tmp_path/"sample.pdf"

    with pymupdf.open() as document:
        page= document.new_page()
        page.insert_text((72,72), "Hello study memory")
        document.new_page()
        document.save(str(pdf_path))
    
    records = extract_pages(pdf_path, "TEST")
    output_path = tmp_path/"processed"/"sample.json"

    save_records(records, output_path)
    loaded_records = load_records(output_path)

    assert len(loaded_records) == 2
    assert loaded_records[0]["page"] == 1
    assert loaded_records[-1]["page"] == 2
    assert loaded_records == records
    assert loaded_records[1]["text"].strip() == ""