"""Abstract Ingestor interface."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract Class for all the different Importing classes."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check if file can be ingested."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Pass for other parsers to define."""
        pass
