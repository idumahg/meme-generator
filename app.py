"""A basic flask server code for web interface."""
import random
import os
import PIL
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all necessary resources.

    Parameters (None)

    Returns:
        quotes (List): list of quotes from supported file type.
        imgs (List): list of images to be manipulated.
    """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    quote = random.choice(quotes)
    img = random.choice(imgs)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    tmp = f'./tmp/{random.randint(0, 100000000)}.jpg'

    try:
        img_content = requests.get(image_url, stream=True).content
        with open(tmp, 'wb') as img:
            img.write(img_content)

        quote_body = request.form['body']
        quote_author = request.form['author']
        path = meme.make_meme(tmp, quote_body, quote_author)
        os.remove(tmp)
        return render_template('meme.html', path=path)
    except (requests.exceptions.ConnectionError, PIL.UnidentifiedImageError):
        os.remove(tmp)
        return render_template('meme_error.html')


if __name__ == "__main__":
    app.run()
