from core.base_scraper import BaseScraper
from core.logger import logger

class GetStandingsCumulativeScraper(BaseScraper):
  def scrape(self):
    logger.info("Iniciando scraping de la tabla de posiciones del acumulado...")
    html = self.fetch_html()
    soup = self.get_soup(html)
    
    tbody_tag = soup.find("tbody")
    
    data = []
    for row in tbody_tag.find_all("tr"):
      cols = row.find_all("td")
      
      if len(cols) < 10:
        continue
      
      position = cols[0].get_text(strip=True)
      team_cell = cols[1]
      team_spans = team_cell.find_all("span") if team_cell else []
      teamFullname = team_spans[0].get_text(strip=True) if len(team_spans) > 0 else ""
      teamName = team_spans[1].get_text(strip=True) if len(team_spans) > 1 else ""
      
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