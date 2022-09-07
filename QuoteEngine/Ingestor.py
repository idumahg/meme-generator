from typing import List
from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """
    A class that encapsulates all the ingestors to provide one interface to load any supported file type.
    """
    files = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]  # List of files to be parsed.

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        A class method to parse files from any supported file type

        Parameters:
            path (str): The path to the files to be ingested

        Returns:
            quotes (List): A list containing quotes from the selected file type.
        """
        for file in cls.files:
            if file.can_ingest(path):
                return file.parse(path)
