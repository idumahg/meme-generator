# Meme generator
A meme generator app that generates images with quotes inscribed onto them. 

## Table of Contents
* [Overview of project](#overview)
* [Instruction for setting up](#instruction)
* [General info](#info)

## Overview of project
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. The quotes come from a variety of file types (PDF, TXT, DOCX and TXT). Hence we engineer a solution to extract each quote line-by-line from these files and save the images. 

There are sample quotes and images of Xander the pup in the folder. However, the app also accepts dynamic user input through a command-line too and a web service. So users can provide any image, together with a quote (with a body and author), and get an image with the quote inscribed onto the image.

## Instruction for setting up
* Quote Engine: This module is composed of classes that ingest different file types that contain quotes. It contains:
  * An abstract base class **IngestorInterface** that contains class method signature.
  * An **Ingestor** class that realize the **IngestorInterface** class and encapsulates all the ingestors to provide one interface to load any supported    file type.
  * A **QuoteModel** class to encapsulate the body and author of a quote.
  * Ingestor classes (DocxIngestor, TextIngestor, PDFIngestor, CSVIngestor) to ingest file types.
* *meme.py* is a simple CLI code that can be run from the terminal. It takes in three *optional* CLI arguuments:
  * \--body: a string quote body
  * \--author: a string quote author
  * \--path: an image path
  
  The script returns a path to a generated image. If any argument is not defined, a random selection is used.
* *app.py* is a flask app starter code. This code uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image. It uses the *requests* package to fetch an image from a user submitted URL.
* 
Example quotes are provided in   _./\_data/SimpleLines_ and  _./\_data/DogQuotes_


