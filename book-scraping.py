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

tabla = soup.find_all('table')[0]
tabla_paises = tabla.find_all('tr')
# ...existing code...

tabla = soup.find_all('table')[0]
tabla_paises = tabla.find_all('tr')

datos = []

for fila in tabla_paises:
    # Extraer el nombre del país del primer th
    th = fila.find('th')
    if th:
         span = th.find('span')
         if span:
                nombre = span.get_text(strip=True)
    else:
        continue  # Si no hay th, no es una fila válida

    # Extraer la fecha de admisión del primer td (o segundo td si el primero no es fecha)
    tds = fila.find_all('td')
    fecha = ""
    if tds:
        # Busca el primer td que tenga una fecha (usualmente contiene un número y "de")
        for td in tds:
            texto_td = td.get_text(strip=True)
            #Como hay registros que su segunda columna no es fecha, se verifica que contenga un mes
            if any(mes in texto_td for mes in ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]):
                fecha = texto_td
                break
        if not fecha:
            fecha = tds[0].get_text(strip=True)  # Si no encuentra, toma el primero dato
    else:
        fecha = ""

    # Solo agrega si hay nombre y fecha
    if nombre and fecha:
        datos.append({"pais": nombre, "fecha": fecha})
# Imprimir los datos extraídos
#for fila in datos:
  #  print(fila)

#Los datos extraídos se guardan en un archivo csv
df = pd.DataFrame(datos)
df.to_csv('paises.csv', index=False, header=False)

# Guardar en JSON
with open('paises.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)

# ...existing code...


time.sleep(2)

