from core.base_scraper import BaseScraper
from core.logger import logger

class GetTeamScraper(BaseScraper):
  def scrape(self):
    logger.info("Iniciando scraping de la plantilla del equipo...")

    html = self.fetch_html()
    soup = self.get_soup(html)

    div_cards = soup.find_all("div", class_="post_jugador")
    data = []

    for row in div_cards:
      # Imagen del jugador
      img_tag = row.find("img")
      img_src = img_tag.get("src") if img_tag else ""
      full_image_url = f"https://universitario.pe{img_src}"

      # Dorsal del jugador
      dorsal_tag = row.find("p", class_="p_numero")
      dorsal = dorsal_tag.get_text(strip=True) if dorsal_tag else ""

      # Nombre y apellido
      name_tag = row.find("a", href="#")
      full_name = name_tag.get_text(strip=True) if name_tag else ""
      parts = full_name.split()

      first_name = parts[0] if len(parts) > 0 else ""
      last_name = " ".join(parts[1:]) if len(parts) > 1 else ""

      data.append({
        "image": full_image_url,
        "numberDorsal": dorsal,
        "firstName": first_name,
        "lastName": last_name,
      })
      
    return data