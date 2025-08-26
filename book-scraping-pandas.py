import pandas as pd
import requests as req
from bs4 import BeautifulSoup
import time
import json
import sys
from io import StringIO

class Scraper:
    
    URL_BASE = 'https://es.wikipedia.org/wiki/Estado_miembro_de_las_Naciones_Unidas'
    TABLE_CLASS = 'wikitable sortable sticky-header sort-under'

    def scrapeWiki(self, URL_BASE=URL_BASE, TABLE_CLASS=TABLE_CLASS):
        # 1. Obtención del HTML
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        info_obtenida = req.get(URL_BASE, headers=headers)

        print("Status Code:", info_obtenida.status_code)  # Para depuración

        if info_obtenida.status_code == 200:  # Verifica que la solicitud fue exitosa
            html_obtenido = info_obtenida.text
            
        else:
            print(f"Error al obtener la página: {info_obtenida.status_code}")
            sys.exit()

        # 2. Parseo del HTML
        soup = BeautifulSoup(html_obtenido, "html.parser")

        print('###################################')  

        tables = soup.find('table', class_=TABLE_CLASS)

        #StringIO convierte un string en un objeto tipo archivo, útil para funciones que requieren 
        # archivos pero los datos se encuentran en texto.
        df = pd.read_html(StringIO(str(tables)))[0]

        print(df)

        df.to_csv('paises-2.csv', index=False, encoding='utf-8-sig')
        df.to_json('paises-2.json', orient='records', force_ascii=False)

        # Pausa de 2 segundos entre cada solicitud para evitar sobre cargar el servidor
        time.sleep(2)

wiki_scraper = Scraper()
wiki_scraper.scrapeWiki()