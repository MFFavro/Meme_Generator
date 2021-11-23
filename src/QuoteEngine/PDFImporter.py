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

        temp = f'./temp_{random.randint(0,100000)}.txt'
        cmd = ['pdftotext','-layout', path, temp]
        call = subprocess.call(cmd)

        file_ref = open(temp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\r\n').strip()
            if len(line) > 0:
                parse = line.split('-')
                nq = QuoteModel(parse[0].strip().strip('"'), parse[1].strip())
                quotes.append(nq)

        file_ref.close()
        os.remove(temp)
        return quotes
