from core.base_scraper import BaseScraper
from core.logger import logger

class GetTournamentMatchesScraper(BaseScraper):
  def format_date(self, fecha):
    # "Viernes, 18 Julio 2025" -> "Vier, 18 Jul."
    dias = {
        "Lunes": "Lun",
        "Martes": "Mar",
        "Miércoles": "Mié",
        "Jueves": "Jue",
        "Viernes": "Vier",
        "Sábado": "Sáb",
        "Domingo": "Dom"
    }
    meses = {
        "Enero": "Ene", "Febrero": "Feb", "Marzo": "Mar", "Abril": "Abr",
        "Mayo": "May", "Junio": "Jun", "Julio": "Jul", "Agosto": "Ago",
        "Septiembre": "Sep", "Octubre": "Oct", "Noviembre": "Nov", "Diciembre": "Dic"
    }
    try:
        dia_semana, resto = fecha.split(",", 1)
        partes = resto.strip().split(" ")
        dia = partes[0]
        mes = meses.get(partes[1], partes[1])
        return f"{dias.get(dia_semana.strip(), dia_semana[:3])}, {dia} {mes}."
    except Exception:
        return fecha
      
  def format_hour(self, hora):
    # "3:30 PM" -> "3:30 p.m."
    return hora.replace("AM", "a.m.").replace("PM", "p.m.").replace("am", "a.m.").replace("pm", "p.m.")
  
  def format_response(self, data):
    grouped = {}
    for fixture in data:
      fixture_name = fixture.get("fixture_date")
      matches = []

      for match in fixture.get("matches", []):
          home = match["home_team"]["name"]
          away = match["away_team"]["name"]

          # ✅ Filtrar solo los partidos de Universitario
          if "Universitario" not in (home, away):
              continue

          month = match["date"].split(" ")[-2]
          
          if month not in grouped:
            grouped[month] = []

          grouped[month].append({
              "home_team": match["home_team"],
              "away_team": match["away_team"],
              "date": self.format_date(match["date"]),
              "competition": match["competition"],
              "status": match["status"],
              "match_current_time": match["match_current_time"],
              "hour_match": self.format_hour(match["hour_match"])
          })

      # Solo agregar si hay partidos de Universitario en ese fixture
      result = []
      for month, matches in grouped.items():
        result.append({
          "date": month,
          "matches": matches
        })
    return result
  
  def scrape(self):
    logger.info("Iniciando scraping de los encuentros del torneo...")
    html = self.fetch_html()
    soup = self.get_soup(html)
    
    data = []
    ul_tag = soup.select_one("ul.list.accordion")
    for date in ul_tag.find_all("li", class_="fase card"):
      div_header = date.select_one("div.card-header")
      textDate = div_header.find("h3").get_text(strip=True)
      
      matches = []
      div_matches = date.select_one("div.collapse")
      ul_matches = div_matches.find("ul")
      for match in ul_matches.find_all("li", class_="fase"):
        div_match_date = match.select_one("div.event-date")
        matchDate = div_match_date.find("span").get_text(strip=True)
 
        div_events = match.select_one("div.event-wrapper")
        for event in div_events.find_all("div", class_="event-body"):
          classes = event.get("class", [])
          homeTeam = event.select_one("div.local-team").find("span", class_="team-name d-md-none").get_text(strip=True)
          awayTeam = event.select_one("div.visit-team").find("span", class_="team-name d-md-none").get_text(strip=True)
          
          matchScore = event.select_one("div.match-result").find_all("span", class_=False)
          
          matchTime = event.select_one("div.match-time").find("span", class_="timer").get_text(strip=True)
          matchHour = event.select_one("div.match-hour").get_text(strip=True)
          
          if "finished" in classes:
            stateMatch = "finished"
          elif "without-starting" in classes:
            stateMatch = "without-starting"
          elif "started" in classes:
            stateMatch = "started"
          else:
            stateMatch = "undefined"
          
          matches.append({
            "home_team": {
              "name": homeTeam,
              "score": matchScore[0].get_text(strip=True) if len(matchScore) > 0 else "0"
            },
            "away_team": {
              "name": awayTeam,
              "score": matchScore[2].get_text(strip=True) if len(matchScore) > 0 else "0"
            },
            "date": matchDate,
            "competition": "Liga 1",
            "status": stateMatch,
            "match_current_time": matchTime,
            "hour_match": matchHour
          })
      
      data.append({
        "fixture_date": textDate,
        "matches": matches
      })
    return self.format_response(data)