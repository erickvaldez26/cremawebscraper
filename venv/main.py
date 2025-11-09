from scrapers.recent_news import RecentNewsScraper
from scrapers.all_news import AllNewsScraper
from scrapers.get_standings_opening import GetStandingsOpeningScraper
from scrapers.get_standings_closing import GetStandingsClosingScraper
from scrapers.get_standings_cumulative import GetStandingsCumulativeScraper
from scrapers.get_tournament_matches import GetTournamentMatchesScraper
from core.storage import save_csv, save_json

def main():
  # Obtener solo las 3 noticias recientes
  recentNewsScraper = RecentNewsScraper("https://universitario.pe/")
  dataRecentNews = recentNewsScraper.scrape()
  save_json(dataRecentNews, "recent_news")
  print(f"✅ Se guardaron {len(dataRecentNews)} registros en data/processed/")
  
  # Obtener todas las noticias de universitario
  allNewsScraper = AllNewsScraper("https://universitario.pe/noticias")
  dataAllNews = allNewsScraper.scrape()
  save_json(dataAllNews, "all_news")
  print(f"✅ Se guardaron {len(dataAllNews)} registros en data/processed/")
  
  # Obtener la tabla de posiciones Liga 1 - Apertura
  standingsOpeningScraper = GetStandingsOpeningScraper("https://www.futbolperuano.com/liga-1/tabla-de-posiciones")
  dataTableOpening = standingsOpeningScraper.scrape()
  save_json(dataTableOpening, "standings_opening")
  print(f"✅ Se guardaron {len(dataTableOpening)} registros en data/processed/")
  
  # Obtener la tabla de posiciones Liga 1 - Clausura
  standingsClosingScraper = GetStandingsClosingScraper("https://www.futbolperuano.com/liga-1/clausura/tabla-de-posiciones")
  dataTableClosing = standingsClosingScraper.scrape()
  save_json(dataTableClosing, "standings_closing")
  print(f"✅ Se guardaron {len(dataTableClosing)} registros en data/processed/")
  
  # Obtener la tabla de posiciones Liga 1 - Acumulado
  standingsCumulativeScraper = GetStandingsCumulativeScraper("https://www.futbolperuano.com/liga-1/clausura/tabla-de-posiciones")
  dataTableCumulative = standingsCumulativeScraper.scrape()
  save_json(dataTableCumulative, "standings_cumulative")
  print(f"✅ Se guardaron {len(dataTableCumulative)} registros en data/processed/")
  
  tournamentMatchesScraper = GetTournamentMatchesScraper("https://www.futbolperuano.com/liga-1/clausura/")
  dataTournamentMatches = tournamentMatchesScraper.scrape()
  save_json(dataTournamentMatches, "tournament_matches")
  print(f"✅ Se guardaron {len(dataTournamentMatches)} registros en data/processed/")
  
if __name__ == "__main__":
  main()