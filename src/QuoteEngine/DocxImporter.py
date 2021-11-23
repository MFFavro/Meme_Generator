"""Importer for Docx files."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    """Helper to read Docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str):
        """Parse Docx file and make list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
