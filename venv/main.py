# --- Librerías estándar ---
import sys
import time

# --- Librerías de terceros ---
# (Ej: requests, firebase_admin, etc.)

# --- Módulos del proyecto ---
from scrapers.recent_news import RecentNewsScraper
from scrapers.all_news import AllNewsScraper
from scrapers.get_standings_opening import GetStandingsOpeningScraper
from scrapers.get_standings_closing import GetStandingsClosingScraper
from scrapers.get_standings_cumulative import GetStandingsCumulativeScraper
from scrapers.get_tournament_matches import GetTournamentMatchesScraper
from scrapers.get_team import GetTeamScraper
from core.storage import save_csv, save_json
from core.firebase_config import init_firebase
from core.notifications import send_discord_message

def main():
  try:
    print("🔥 Iniciando aplicación...", flush=True)
    db = init_firebase()
    
    # Limpiar base de datos
    print("🧹 Limpiando colecciones...", flush=True)
    for col in ["recent_news", "all_news", "standings", "matches"]:
      clear_collection(db, col)
    print("✅ Base de datos limpiada", flush=True)
    
    # Subir datos
    upload_news(db)
    upload_standings(db)
    upload_matches(db)
    upload_team(db)
    
    print("⏳ Esperando antes de cerrar contenedor...", flush=True)
    time.sleep(4)
    send_discord_message(
      "Scraping finalizado", 
      "El proceso de scraping ha terminado correctamente y los datos fueron actualizados en Firebase."
    )
    print("🔥🔥🔥 Desplegado correctamente 🔥🔥🔥")
  except Exception as e:
    send_discord_message(f"❌ Error en el scraping: {e}")


def clear_collection(db, collection_name):
  """Elimina todos los documentos dentro de una colección de Firestore."""
  docs = db.collection(collection_name).stream()
  for count, doc in enumerate(docs, start=1):
    doc.reference.delete()
  print(f"🧹 {collection_name} limpiada ({count} documentos eliminados)", flush=True)


def upload_news(db):
  """Obtiene y guarda noticias recientes y todas las noticias."""
  print("📰 Obteniendo noticias...", flush=True)

  recent = RecentNewsScraper("https://universitario.pe/").scrape()
  for item in recent:
    db.collection("recent_news").document().set(item)
  print(f"✅ {len(recent)} noticias recientes guardadas", flush=True)

  all_news = AllNewsScraper("https://universitario.pe/noticias").scrape()
  for item in all_news:
    db.collection("all_news").document().set(item)
  print(f"✅ {len(all_news)} noticias generales guardadas", flush=True)


def upload_standings(db):
  """Obtiene y guarda las tablas de posiciones."""
  print("📊 Obteniendo tablas de posiciones...", flush=True)

  scrapers = [
    ("apertura", GetStandingsOpeningScraper("https://www.futbolperuano.com/liga-1/tabla-de-posiciones")),
    ("clausura", GetStandingsClosingScraper("https://www.futbolperuano.com/liga-1/clausura/tabla-de-posiciones")),
    ("acumulado", GetStandingsCumulativeScraper("https://www.futbolperuano.com/liga-1/tabla-acumulada/tabla-de-posiciones")),
  ]

  for name, scraper in scrapers:
    data = scraper.scrape()
    db.collection("standings").document(name).set({
      "tournament": name.capitalize(),
      "teams": data
    })
  print(f"✅ {len(data)} equipos guardados en {name}", flush=True)


def upload_matches(db):
  """Obtiene y guarda los partidos del torneo."""
  print("⚽ Obteniendo partidos del torneo...", flush=True)

  scraper = GetTournamentMatchesScraper("https://www.futbolperuano.com/liga-1/clausura/")
  data = scraper.scrape()
  for month_data in data:
    db.collection("matches").document(month_data["date"]).set(month_data)
  print(f"✅ {len(data)} meses de partidos guardados", flush=True)

def upload_team(db):
  """Obtiene y guarda la pantilla del equipo."""
  print("Obteniendo plantilla del equipo...", flush=True)
  
  scraper = GetTeamScraper("https://universitario.pe/equipo/futbol-masculino")
  data = scraper.scrape()
  for item in data:
    db.collection("team").document().set(item)
  print(f"✅ {len(data)} jugadores guardados", flush=True)


if __name__ == "__main__":
  main()