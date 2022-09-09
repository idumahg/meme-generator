"""A code to manipulate and draw text onto images."""
from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import QuoteModel
import os
import random
import textwrap


class MemeEngine:
    """
    A Meme Engine class to manipulate and insert text onto images.

    Attributes:
        out_dir (str): the directory to save output image.
    """

    def __init__(self, out_dir):
        """Initialize the memeEngine class attribute."""
        self.out_dir = out_dir

        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Make meme Module to save manipulated image to output directory.

        Parameters:
            img_path (str): The file location for input image.
            text (str): The body of the quote.
            author (str): The author of the quote.
            width (int): The pixel width value. Default=500.

        Returns:
            save_path (str): The file path to the output image.
        """
        img = Image.open(img_path)

        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/arial.ttf', 20)
            message = repr(QuoteModel(text, author))
            message = "\n".join(textwrap.wrap(message,
                                              width=40))  # from stack exchange
            x = random.randint(5, width // 4)
            y = random.randrange(5, height - 50)
            draw.text((x, y), message,
                      font=font, fill='black', align='center')

        save_path = f'{self.out_dir}/{str(random.randint(10000, 99999))}.jpg'
        img.save(save_path)

        return save_path
