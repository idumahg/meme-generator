from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import QuoteModel
import os
import random


class MemeEngine:
    """
    A Meme Engine class to manipulate and insert text onto images.
    
    Attributes:
        out_dir (str): the directory to save output image.
    """

    def __init__(self, out_dir):
        self.out_dir = out_dir

        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        A make meme Module to save manipulated image to output directory.

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
            draw.text((10, 30), message, font=font, fill='black')

        save_path = f'{self.out_dir}/{str(random.randint(10000, 99999))}.jpg'
        img.save(save_path)
        return save_path
