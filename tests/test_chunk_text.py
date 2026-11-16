from chunk_text import chunk_pages
from extract_pdf import load_records, save_records

def test_chunk_pages_keeps_short_tail_and_skips_blank_page():
    records = [
        {"course": "TEST", "document": "sample.pdf", "page": 1, "text": "ABCDEFGHIJK"},
        {"course": "TEST", "document": "sample.pdf", "page": 2, "text": ""},
        {"course": "TEST", "document": "sample.pdf", "page": 3, "text": "LMNOP"},
    ]

    chunks = chunk_pages(records, chunk_size=5)

    assert [chunk["page"] for chunk in chunks] == [1,1,1,3]
    assert [chunk["chunk_number"] for chunk in chunks] == [1,2,3,1]

    page_1_text = "".join(chunk["text"] for chunk in chunks if chunk["page"] == 1)
    assert page_1_text == "ABCDEFGHIJK"


def test_chunks_survive_save_and_load(tmp_path):
    records = [
        {"course": "TEST", "document": "sample.pdf", "page": 1, "text": "ABCDEFGHIJK"},
        {"course": "TEST", "document": "sample.pdf", "page": 2, "text": ""},
        {"course": "TEST", "document": "sample.pdf", "page": 3, "text": "LMNOP"},
    ]

    chunks = chunk_pages(records, chunk_size=5)
    output_path = tmp_path / "chunks.json"

    save_records(chunks, output_path)
    loaded_chunks = load_records(output_path)

    assert loaded_chunks == chunks
    assert [chunk["page"] for chunk in loaded_chunks] == [1, 1, 1, 3]
    assert [chunk["chunk_number"] for chunk in loaded_chunks] == [1, 2, 3, 1]