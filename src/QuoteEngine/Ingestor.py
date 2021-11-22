"""Ingestor for all file types."""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TextImporter import TextImporter


class Ingestor(IngestorInterface):
    """Ingestor for all file types."""

    importers = [DocxImporter, CSVImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path: str):
        """Parse a file and make a list."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
