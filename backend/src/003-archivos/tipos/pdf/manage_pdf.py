#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdfkit  # pip3 install pdfkit

URL = "https://www.google.es/search?source=hp&q=tensor_flow"
ARCHIVO = "google_search_tensorflow.pdf"

# Descargar una web en PDF
pdfkit.from_url(URL, ARCHIVO)

# =================================================================

# Extraer el contenido de un archivo PDF  (pip3 install pdfminer3k)
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

def readPDF(pdfFile):
    rm = PDFResourceManager()
    str_buff = StringIO()
    laparams = LAParams()
    device = TextConverter(rm, str_buff, laparams=laparams)

    process_pdf(rm, device, pdfFile)
    device.close()

    content = str_buff.getvalue()
    str_buff.close()
    return content

with open(ARCHIVO, "rb") as f:
    output = readPDF(f)

"""
Fuentes:
https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python
https://github.com/mudspringhiker/parsing_pdf_pdfminer3k/blob/master/read_pdf.py
"""
