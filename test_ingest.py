from ingestor.pdf_ingest import ingest_pdf
from ingestor.web_ingest import ingest_web

def test_ingest_pdf():
    assert "PDF content" in ingest_pdf("dummy.pdf")

def test_ingest_web():
    assert "Web content" in ingest_web("http://example.com")