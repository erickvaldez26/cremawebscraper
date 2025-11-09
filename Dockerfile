FROM python:3.11-slim

# --- Configurar directorio de trabajo ---
WORKDIR /app

# --- Copiar solo lo necesario ---
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# --- Copiar el código del proyecto ---
COPY . .

# --- Variable de entorno para mostrar logs en tiempo real ---
ENV PYTHONUNBUFFERED=1

# --- Comando principal ---
CMD ["python", "venv/main.py"]
