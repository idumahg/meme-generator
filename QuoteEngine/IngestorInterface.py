from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    An abstract base class that defines how children classes should be defined.
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        A class method to check if file extension is in allowed extensions.

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
        """
        Abstract method that will be defined in children classes.
        """
        pass
