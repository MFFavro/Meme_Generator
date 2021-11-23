"""Importer for CSV files."""
from typing import List
import csv
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    """Helper to read CSV file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str):
        """Parse CSV file and create list."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []

        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
