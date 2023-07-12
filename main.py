# boto3 is a client library for python which allows connections to various Amazon Web Services
# One of these AWS is Amazon Polly which is an API enabling text to speech
# Link to documentation for polly
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html
import boto3
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog as fido
import os


def choose_pdf():
    chosen_pdf_filepath = fido.askopenfilename(title="Pick your pdf")

    def pdf_to_audio():

        # Create a pdf reader object. The PdfReader class takes a positional argument of the path to the pdf file.
        reader = PdfReader(chosen_pdf_filepath)

        text = ""
        # printing number of pages in pdf file
        for page in reader.pages:  # Loop through all the pages in the PDF document

            # Extract the text from each page
            text += page.extract_text()

        # Create a client for the Polly service
        polly = boto3.client(
            "polly",  # Choose Polly service
            region_name='eu-west-2',
            aws_access_key_id=os.environ["ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["SECRET_ACCESS_KEY"]
        )

        # Use the client to synthesize a text input
        response = polly.synthesize_speech(Text=text, VoiceId="Joanna", OutputFormat="mp3")

        # The response returns the following syntax:
        # {
        #     'AudioStream': StreamingBody(),
        #     'ContentType': 'string',
        #     'RequestCharacters': 123
        # }
        # AudioStream is a stream containing the synthesized speech. So it is taken from the response here
        body = response["AudioStream"].read()

        # Create a file
        # "wb" means "write and binary"
        with open("output.mp3", "wb") as file:
            file.write(body)  # Write the audio stream as text in to the file. Any mp3 viewer can open this as audio

    pdf_to_audio()


def quit_app():
    window.quit()


window = tk.Tk()
window.title("PDF to Audiobook App")
window.config(padx=50, pady=50, bg="white", highlightthickness=0)

canvas = tk.Canvas(width=1000, height=500, bg="white", highlightthickness=0)
logo_image = tk.PhotoImage(file="logo.png")
canvas.create_image(500, 220, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

pdf_button = tk.Button(text="Choose PDF", bg="white", highlightthickness=0, command=choose_pdf)
pdf_button.grid(row=1, column=0)

exit_button = tk.Button(text="Exit", bg="white", highlightthickness=0, command=quit_app)
exit_button.grid(row=1, column=2)

window.update()
window.mainloop()
