import subprocess
import os
import uuid
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """
    A class to ingest pdf files. This class inherits the IngestorInterface abstract class.
    """

    allowed_extensions = ['pdf']  # allowed extension for the PDFIngestor class

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        A class method to parse lines from pdf files.

        Parameters:
            path (str): The path to the files to be ingested

        Raises:
            Exception: Must be a pdf file, else an exception is raised.

        Returns:
            quotes (List): A list containing quotes from pdf files.
        """

        if not cls.can_ingest(path):
            raise Exception('File format not supported')

        if not os.path.exists('./tmp'):
            os.mkdir('./tmp')

        tmp = f'./tmp/{str(uuid.uuid4())}.txt'  # temporary file to be deleted
        subprocess.run(['pdftotext', '-layout', path, tmp])

        with open(tmp, "r") as f:
            quotes = []
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)

        os.remove(tmp)
        return quotes
