from pypdf import PdfReader
from tkinter import filedialog as fd
import tkinter as tk
filename = fd.askopenfilename()

reader = PdfReader(filename)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()