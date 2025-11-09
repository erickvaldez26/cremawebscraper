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

## ⚙️ Se desplego en Railway

El proyecto utiliza Firebase Firestore como base de datos para almacenar la información procesada por los scrapers.
Por motivos de seguridad, la clave privada (serviceAccountKey.json) no se incluye en el repositorio.
En su lugar, las credenciales se configuran mediante una variable de entorno llamada FIREBASE_KEY en Railway.

Esta variable contiene el contenido completo del archivo JSON de servicio de Firebase y es leída por el script de inicialización (firebase_config.py) para establecer la conexión segura con Firestore.

De esta forma, las credenciales se mantienen seguras, el proyecto puede desplegarse sin archivos sensibles y la conexión con Firebase se realiza automáticamente tanto en local como en producción.

La ejecución periodica se hace a las 3:00 a.m.

## 🕹️ Ejecución local

**Recuerda siempre tener el archivo de las credenciales de firebase**

1. Instalar dependencias (Solo la primera vez o si se agregan librerias)

```bash
pip install -r requirements.txt
```

2. Activar el venv (Ubicarse dentro de la carpeta venv)

```bash
source venv/bin/activate
```

3. Comando final para ejecutar el proyecto

```bash
python main.py
```
