"""A code that defines an abstract base class."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class that provides template for children classes."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Class method to check if file extension is in allowed extensions.

        Parameters:
            path (str): path to the file to be ingested

        Returns:
            bool: True if file is in allowed extensions, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method that will be defined in children classes."""
        pass
