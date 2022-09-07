import docx
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """
    A class to ingest docx files. This class inherits the IngestorInterface abstract class.
    """

    allowed_extensions = ['docx']   # allowed extension for the DocxIngestor class

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        A class method to parse lines from docx files.

        Parameters:
            path (str): The path to the files to be ingested

        Raises:
            Exception: Must be a docx file, else an exception is raised

        Returns:
            quotes (List): A list containing quotes from docx files.
        """

        if not cls.can_ingest(path):
            raise Exception('file format not supported')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)

        return quotes
