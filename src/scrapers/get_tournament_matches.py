from core.base_scraper import BaseScraper
from core.logger import logger

class GetTournamentMatchesScraper(BaseScraper):
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
              "score": matchScore[0].get_text(strip=True)
            },
            "away_team": {
              "name": awayTeam,
              "score": matchScore[2].get_text(strip=True)
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
      
    return data