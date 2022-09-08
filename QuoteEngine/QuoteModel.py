class QuoteModel:
    """
    A class to encapsulate the body and author of a quote.

    Attributes:
        body (str): The body of the quote.
        author (str): The author of the quote.
    """

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Returns a printable representation of the class"""
        if self.body[0] == '"':
            return f'{self.body} - {self.author}'
        else:
            return f'"{self.body}" - {self.author}'

