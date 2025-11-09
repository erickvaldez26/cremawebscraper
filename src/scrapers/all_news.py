from core.base_scraper import BaseScraper
from core.logger import logger

class AllNewsScraper(BaseScraper):
  def scrape(self):
    logger.info("Iniciando scraping de Todas las noticias...")
    html = self.fetch_html()
    soup = self.get_soup(html)
    
    div = soup.find("div", class_="link_noticias")
    
    news = []
    for new in div.select(".post_noticia"):
      img_tag = new.find("img")
      imgUrl = img_tag["src"] if img_tag else None
      fullImgUrl = "https://universitario.pe" + imgUrl
      p_tag = new.find("p", class_="p_date_category")
      date = p_tag.contents[0].strip()
      category = p_tag.find("a").text.strip()[2:]
      a_tag = new.select_one(".titular_noticia > a:not([class])")
      title = a_tag.get_text(strip=True) if a_tag else None
      news.append({"image": fullImgUrl, "date": date, "category": category, "title": title})
    
    return news