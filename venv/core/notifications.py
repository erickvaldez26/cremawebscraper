import requests
import datetime
import os

def send_discord_message(title, message, color=0x7289DA):
  """
  Envia un mensaje al canal de Discord usando un webhook.
  """
  webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
  if not webhook_url:
    print("⚠️ No se encontró la variable DISCORD_WEBHOOK_URL")
    return
  
  timestamp = datetime.datetime.utcnow().isoformat()
  
  embed = {
    "title": f"⚙️ {title}",
    "description": f"```py\n{message}\n```",
    "color": color,
    "footer": {
      "text": "Crema Web Scraper • Render • Python 🐍",
    },
    "timestamp": timestamp,
    "author": {
      "name": "Universitario de Deportes Data Bot 🤖",
    },
    "fields": [
      {
        "name": "Estado",
        "value": "✅ Ejecución completada con éxito",
        "inline": False
      },
    ]
  }
  
  data = {
    "username": "Scraper Bot 🧠",
    "embeds": [embed]
  }
  
  try:
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
      print("✅ Mensaje enviado a Discord")
    else:
      print(f"❌ Error al enviar mensaje a Discord: {response.text}")
  except Exception as e:
    print(f"❌ Error de conexión a Discord: {e}")