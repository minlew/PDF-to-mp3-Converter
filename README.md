# PDF to Audiobook Converter

## Description
This project provides a simple GUI application that converts PDF files to audiobooks using Amazon's Polly text-to-speech service.

### Features

* User-friendly graphical interface
* PDF file selection via file dialog
* Conversion of PDF text to speech using Amazon Polly
* Output saved as an MP3 file

### Technologies
* Python
* Amazon Polly

### Python Libs
* Tkinter
* boto3
* PyPDF2

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Install [requirements](requirements.txt).
4. Run [script](main.py) in Python. 

## Usage
1. Click the "Choose PDF" button to select your PDF file.
2. The application will convert the PDF to an MP3 file named `output.mp3` in the same directory.
3. To exit the application, click the "Exit" button.

## Customization
* The application uses the "Joanna" voice from Amazon Polly. You can change this by modifying the `VoiceId` parameter in the `polly.synthesize_speech()` function call.
The AWS region is set to `eu-west-2`. You can change this in the `boto3.client()` function call if needed.
