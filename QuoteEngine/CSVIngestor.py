import pandas as pd
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """
    A class to ingest CSV files. This class inherits the IngestorInterface abstract class.
    """

    allowed_extensions = ['csv']  # allowed extension for the CSVIngestor class

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        A class method to parse lines from csv files.

        Parameters:
            path (str): The path to the files to be ingested

        Raises:
            Exception: Must be a csv file, else an exception is raised

        Returns:
            quotes (List): A list containing quotes from csv files.
        """

        if not cls.can_ingest(path):
            raise Exception('file format not supported')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
