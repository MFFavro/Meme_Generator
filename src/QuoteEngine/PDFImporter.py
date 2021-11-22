"""Import a PDF File."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    """Helper to read PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """Parse a PDF file and make a list."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./temp_{random.randint(0,100000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp], shell=True)

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                nq = QuoteModel(parse[0].strip().strip('"'), parse[1].strip())
                quotes.append(nq)

        file_ref.close()
        os.remove(tmp)
        return quotes
