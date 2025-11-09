from scrapers.recent_news import RecentNewsScraper
from scrapers.all_news import AllNewsScraper
from scrapers.get_standings_opening import GetStandingsOpeningScraper
from scrapers.get_standings_closing import GetStandingsClosingScraper
from scrapers.get_standings_cumulative import GetStandingsCumulativeScraper
from scrapers.get_tournament_matches import GetTournamentMatchesScraper
from core.storage import save_csv, save_json
from core.firebase_config import init_firebase
import sys
import time

def main():
  print("🔥 Iniciando aplicación...", flush=True)
  sys.stdout.flush()
  
  # Inicializar Firebase
  db = init_firebase()
  
  # Obtener solo las 3 noticias recientes
  recentNewsScraper = RecentNewsScraper("https://universitario.pe/")
  dataRecentNews = recentNewsScraper.scrape()
  for news_item in dataRecentNews:
    db.collection("recent_news").document().set(news_item)
  # save_json(dataRecentNews, "recent_news")
  print(f"✅ Se guardaron {len(dataRecentNews)} registros de noticias recientes en Firestore", flush=True)
  
  # Obtener todas las noticias de universitario
  allNewsScraper = AllNewsScraper("https://universitario.pe/noticias")
  dataAllNews = allNewsScraper.scrape()
  for news_item in dataAllNews:
    db.collection("all_news").document().set(news_item)
  # save_json(dataAllNews, "all_news")
  print(f"✅ Se guardaron {len(dataAllNews)} registros de todas las noticias en Firestore", flush=True)
  
  # Obtener la tabla de posiciones Liga 1 - Apertura
  standingsOpeningScraper = GetStandingsOpeningScraper("https://www.futbolperuano.com/liga-1/tabla-de-posiciones")
  dataTableOpening = standingsOpeningScraper.scrape()
  db.collection("standings").document("apertura").set({
    "tournament": "Apertura",
    "teams": dataTableOpening
  })
  # save_json(dataTableOpening, "standings_opening")
  print(f"✅ Se guardaron {len(dataTableOpening)} registros las posiciones del apertura en Firestore", flush=True)
  
  # Obtener la tabla de posiciones Liga 1 - Clausura
  standingsClosingScraper = GetStandingsClosingScraper("https://www.futbolperuano.com/liga-1/clausura/tabla-de-posiciones")
  dataTableClosing = standingsClosingScraper.scrape()
  db.collection("standings").document("clausura").set({
    "tournament": "Clausura",
    "teams": dataTableClosing
  })
  # save_json(dataTableClosing, "standings_closing")
  print(f"✅ Se guardaron {len(dataTableClosing)} registros las posiciones del clausura en Firestore")
  
  # Obtener la tabla de posiciones Liga 1 - Acumulado
  standingsCumulativeScraper = GetStandingsCumulativeScraper("https://www.futbolperuano.com/liga-1/clausura/tabla-de-posiciones")
  dataTableCumulative = standingsCumulativeScraper.scrape()
  db.collection("standings").document("acumulado").set({
    "tournament": "Acumulado",
    "teams": dataTableCumulative
  })
  # save_json(dataTableCumulative, "standings_cumulative")
  print(f"✅ Se guardaron {len(dataTableCumulative)} registros las posiciones del acumulado en Firestore", flush=True)
  
  tournamentMatchesScraper = GetTournamentMatchesScraper("https://www.futbolperuano.com/liga-1/clausura/")
  dataTournamentMatches = tournamentMatchesScraper.scrape()
  for month_data in dataTournamentMatches:
    month_name = month_data["date"]
    matches = month_data["matches"]
    db.collection("matches").document(month_name).set({
      "date": month_name,
      "matches": matches
    })
  # save_json(dataTournamentMatches, "tournament_matches")
  print(f"✅ Se guardaron {len(dataTournamentMatches)} registros de Partidos en Firestore", flush=True)
  print("🕒 Esperando antes de cerrar contenedor (Railway test)...", flush=True)
  time.sleep(60)
  
if __name__ == "__main__":
  main()