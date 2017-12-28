#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://www.milanuncios.com/anuncios/masajes-relajantes-en-jerez.htm"

# =====================================================

# Prueba sin poder ejecutar el Javascript (bs4 + requests normal)

soup = BeautifulSoup(requests.get(url).content, "html.parser")
print(soup.find(class_="aditem-detail-title"))
#print(soup.prettify())

# ====================================================

# Prueba ejecutando el Javascript con pyvirtualdisplay + selenium

from pyvirtualdisplay import Display  # pip3 install pyvirtualdisplay
from selenium import webdriver
import time

display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Firefox()
browser.get(url)
time.sleep(1)
soup = BeautifulSoup(browser.page_source, "html.parser")
print(soup.find(class_="aditem-detail-title"))
#print(soup.prettify())

# ====================================================

# Fuentes:
# http://koaning.s3-website-us-west-2.amazonaws.com/html/scapingdynamicwebsites.html