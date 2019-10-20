import tkinter as tk
import os, io
from google.cloud import vision
import google.cloud.vision
import pandas as pd
from PIL import Image
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"codecopy-256402-cecfa4ffee2e.json"
client = vision.ImageAnnotatorClient()

HEIGHT = 10
WIDTH = 800
root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

T = tk.Text(root, height=40, width=100)
T.pack(side = 'top')

button = tk.Button(root, text="Get text", bg = 'light gray', fg = 'black', command=lambda: getText())
button.pack(side = 'bottom')
#delete image from the folder
def deleteImage():
    os.remove('image.jpg')
#get text in the image
def getText():
    #open image file
    file_name = 'image.jpg'
    image_path = f'.\VisionAPI\Images\{file_name}'
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    #send image through google vision
    image = vision.types.Image(content=content)
    """
    # or we can pass the image url
    image = vision.types.Image()
    image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
    """
    #get the text
    response = client.document_text_detection(image=image)
    df = pd.DataFrame(columns=['locale', 'description'])
    texts = response.text_annotations
    #display the text on the user interface
    T.insert(tk.END, texts[0].description)
    deleteImage()

root.mainloop()