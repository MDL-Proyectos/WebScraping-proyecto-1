import pandas as pd
import requests as req
from bs4 import BeautifulSoup
import time
import json

URL_BASE = 'https://es.wikipedia.org/wiki/Estado_miembro_de_las_Naciones_Unidas'

# 1. Obtención del HTML
info_obtenida = req.get(URL_BASE)

html_obtenido = info_obtenida.text

# 2. Parseo del HTML
soup = BeautifulSoup(html_obtenido, "html.parser")

# Obtenemos una sección del HTML, filtrando por class
#h2_all = soup.find_all('div', class_="mw-heading mw-heading2")
#print(h2_all)

# Iterar sobre el objeto
#for seccion in h2_all:
#  print('h2: ', seccion.text)

# Se quitan los espacios innecesarios
#for seccion in h2_all:
#  print(seccion.get_text(strip=True))

print('###################################')  

# Todas las etiquetas que tengan el atributo "src"
#src_todos = soup.find_all(src=True)
#for elemento in src_todos:
#  if elemento['src'].endswith(".jpg"):
#    print(elemento)

# Pausa de 2 segundos entre cada solicitud para evitar sobre cargar el servidor

print('###################################')  

# Información de tablas

tabla_paises = soup.find_all('table')[0]
paises = tabla_paises.find_all('tr')
for pais in paises:
    ps = pais.find_all(['th'])
    data = [p.get_text(strip=True) for p in ps]
    print(data)


time.sleep(2)

