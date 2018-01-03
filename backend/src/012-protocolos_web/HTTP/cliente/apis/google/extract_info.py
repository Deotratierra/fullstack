#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from tqdm import tqdm

QUERY = "tensor+flow"
START = 0

URL = "https://www.google.com/search?source=hp&q=%s&start=%d" % (QUERY, START)
content = requests.get(URL).text
soup = BeautifulSoup(content, "lxml")

responses = []
for container in soup.find_all("h3"):
    title = container.text
    href_cont = container.find("a")["href"]
    regex = re.search(r"(?<=/url\?q=)(.+)(?=&sa=U&ved)", href_cont)
    link = regex.group(0)

    responses.append(dict(title=title, link=link))

print("\n\tInformación obtenida de la búsqueda: %s\n" % URL)
pprint(responses)
