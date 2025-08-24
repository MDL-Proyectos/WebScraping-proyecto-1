
# Proyecto de Web Scraping: Estados Miembros de la ONU

Este repositorio contiene la primera etapa del proyecto. En esta fase se realiza un proceso de **Web Scraping** sobre la página de Wikipedia que lista los [Estados miembros de las Naciones Unidas](https://es.wikipedia.org/wiki/Estado_miembro_de_las_Naciones_Unidas).

## 🌐 Objetivo
Extraer información estructurada sobre los países miembros de la ONU desde Wikipedia, para su posterior almacenamiento y análisis en etapas futuras del proyecto (PostgreSQL y ETL).

## 🛠️ Tecnologías utilizadas
- Python 3
- Requests
- BeautifulSoup4
- time (para respetar la infraestructura del sitio)

## 📦 Instalación
Es necesario de tener Python 3 instalado. También instalar las siguientes dependencias necesarias:

```bash
pip install requests beautifulsoup4
```

## ▶️ Ejecución
Ejecutá el script principal para iniciar el scraping:

```bash
python book-scraping.py
```

El script extrae los nombres de los países miembros de la ONU y los guarda en un archivo CSV o JSON para su posterior uso.

## ⚖️ Consideraciones éticas
Este proyecto respeta las buenas prácticas de scraping:
- Se utiliza `time.sleep()` para evitar sobrecargar los servidores de Wikipedia.
- Se accede únicamente a contenido público.
- Se reconoce que Wikipedia ofrece una API oficial como alternativa más eficiente.

## 📁 Estructura del repositorio
```
├── book-scraping.py         # Script principal de scraping
├── paises.csv    # Archivo generado con los datos extraídos en CSV
├── paises.json    # Archivo generado con los datos extraídos en JSON
├── README.md               # Documentación del proyecto
```

## ✍️ Autor
Matias DL
