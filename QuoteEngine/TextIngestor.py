from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """
    A class to ingest txt files. This class inherits the IngestorInterface abstract class.
    """
    allowed_extensions = ['txt']  # allowed extension for the TextIngestor class
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
         A class method to parse lines from txt files.

         Parameters:
             path (str): The path to the files to be ingested

         Raises:
             Exception: Must be a txt file, else an exception is raised.

         Returns:
             quotes (List): A list containing quotes from txt files.
         """

        if not cls.can_ingest(path):
            raise Exception('file format not supported')
            
        quotes = []
        
        with open(path, "r") as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)
            
        return quotes
