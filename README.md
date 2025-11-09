# cremawebscraper

A web scraper for Crema.fm.

# Crema Web Scraper 🧩

**Crema Web Scraper** es un proyecto en **Python** diseñado para recopilar, procesar y estructurar información relevante del club **Universitario de Deportes** desde su sitio web oficial y otras fuentes relacionadas.

El sistema utiliza **BeautifulSoup4**, **Requests** y **Pandas** para extraer, limpiar y estructurar los datos en un formato estándar, permitiendo su uso en aplicaciones móviles, dashboards o almacenamiento en bases de datos como Firebase o PostgreSQL.

## 🚀 Características principales

- Extracción de:

  - Noticias más recientes del club.
  - Información de partidos: estado (_finalizado, en curso, por jugar_), equipos, resultados, fecha y hora.
  - Tablas de posiciones actualizadas (puntos, goles, diferencia de goles, etc.).

- Procesamiento y estructuración automática de datos.
- Integración lista para despliegue en **Render.com**, **Railway.app** o **PythonAnywhere**.
- Compatible con entornos virtuales (`venv`) y dependencias administradas vía `requirements.txt`.

## 🧰 Tecnologías utilizadas

- Python 3.12+
- BeautifulSoup4
- Requests
- Pandas
- LXML
- Logging para monitoreo de ejecución

## ⚙️ Estructura del proyecto

cremawebscraper/
├── src/
│ ├── main.py # Punto de entrada
│ ├── scrapers/ # Módulos de scraping (noticias, tabla, partidos)
│ ├── models/ # Modelos de datos (Match, Team, News, etc.)
│ └── utils/ # Funciones auxiliares
├── requirements.txt
└── README.md

## 🕹️ Ejecución local

```bash
source venv/bin/activate
pip install -r requirements.txt (solo si es la primera vez o cambiaste de ambiente)
python main.py
```
