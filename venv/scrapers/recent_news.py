from core.base_scraper import BaseScraper
from core.logger import logger
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin

class RecentNewsScraper(BaseScraper):
  def scrape(self):
    logger.info("Iniciando scraping de Noticias Recientes...")
    html = self.fetch_html()
    soup = self.get_soup(html)
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    
    for comment in comments:
      if "HOME NOTICIAS" in comment:
        news_node = comment
        break
      
    news_content = []
    for sibling in news_node.next_siblings:
      if isinstance(sibling, Comment) and "videos" in sibling:
        break
      if str(sibling).strip():
        news_content.append(sibling)
        
    soup_news = BeautifulSoup("".join(str(x) for x in news_content), "lxml")
    
    news = []
    for new in soup_news.select(".post_noticia"):
      img_tag = new.find("img")
      imgUrl = img_tag["src"] if img_tag else None
      fullImgUrl = "https://universitario.pe" + imgUrl
      p_tag = new.find("p")
      category = p_tag.get_text(strip=True) if p_tag else None
      a_tag = new.find("a")
      title = a_tag.get_text(strip=True) if a_tag else None
      news.append({"imageNew": fullImgUrl, "date": category, "titleNew": title})
    
    news = news[:3]
    return news