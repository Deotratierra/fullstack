#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import imaplib
# https://docs.python.org/3/library/imaplib.html

# ===========   CONFIGURACIÓN   ===========

#MAIL_ADDRESS = os.environ["GMAIL_ADDRESS"]
#MAIL_PASSWORD = os.environ["GMAIL_PASSWORD"]
SERVER = "imap.gmail.com"

GMAIL_ADDRESS = "mondejar1994@gmail.com"
GMAIL_PASSWORD = "956rajednom"

# ==========================================


# ===============   LOGIN   ================

# Con la función IMAP4_SSL nos conectamos
# de forma segura mediante IMAP a un servidor
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Nos logueamos
result, msg = mail.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
# result devuelve "OK" si todo ha salido bien
print(msg[0].decode("utf-8"))

# =========   BANDEJA DE ENTRADA   =========

# Obtenemos las carpetas de gmail
result, labels = mail.list()
#for label in labels: print(label.decode("ascii"))

# Seleccionamos la bandeja de entrada
result, inbox = mail.select("inbox")

# ==========================================


# ===============   MAILS   ================

# BÚSQUEDA POR IDS
# La funcion search() nos devuelve todos los
# correos en orden cronológico.
# Si borramos el correo con id 1,
# el correo con id 2 pasa a ser el 1

# Buscamos todos los correos
result, data = mail.search(None, "ALL")

# data devuelve una lista de un elemento,
# una cadena de bytes con los
# identificadores de todos los correos,
# ordenados en orden cronológico
mail_ids_list = data[0].split()

# Obtenemos el último email:
result, data = mail.fetch(mail_ids_list[-1], "(RFC822)")

# Obtenemos el cuerpo del documento
body = data[0][1]

# -----------------------------------------

# BÚSQUEDA POR UIDS
# Por identificadores únicos de correos

# Usamos la función uid() y pasamos la cadena
# del comando como primer argumento
result, data = mail.uid("search", None, "ALL")
mail_ids_list = data[0].split()

result, data = mail.uid("fetch", mail_ids_list[-1], "(RFC822)")
print(data)

# ==========================================


# ===========   CERRAR SESIÓN   ============

result, msg = mail.logout()
print(msg[0].decode("utf-8"))

# ==========================================

# Fuente:
# https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/