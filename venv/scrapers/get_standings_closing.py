from core.base_scraper import BaseScraper
from core.logger import logger

class GetStandingsClosingScraper(BaseScraper):
  def scrape(self):
    logger.info("Iniciando scraping de la tabla de posiciones Clausura...")
    html = self.fetch_html()
    soup = self.get_soup(html)
    
    tbody_tag = soup.find("tbody")
    
    data = []
    for row in tbody_tag.find_all("tr"):
      cols = row.find_all("td")
      
      position = cols[0].get_text(strip=True)
      
      team_spans = cols[1].find_all("span")
      teamFullname = team_spans[0].get_text(strip=True)
      teamName = team_spans[1].get_text(strip=True)
      
      matchesPlayed = cols[2].get_text(strip=True)
      matchesWon = cols[3].get_text(strip=True)
      matchesTied = cols[4].get_text(strip=True)
      matchesLost = cols[5].get_text(strip=True)
      goalsScored = cols[6].get_text(strip=True)
      goalsAgainst = cols[7].get_text(strip=True)
      goalDifference = cols[8].get_text(strip=True)
      points = cols[9].get_text(strip=True)
      
      data.append({
        "position": position,
        "teamFullName": teamFullname,
        "teamName": teamName,
        "matchesPlayed": matchesPlayed,
        "matchesWon": matchesWon,
        "matchesTied": matchesTied,
        "matchesLost": matchesLost,
        "goalsScored": goalsScored,
        "goalsAgainst": goalsAgainst,
        "goalDifference": goalDifference,
        "points": points
      })
      
    return data