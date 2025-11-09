import requests
from bs4 import BeautifulSoup

class BaseScraper:
  def __init__(self, base_url: str):
    self.base_url = base_url

  def fetch_html(self, url: str = None):
    url = url or self.base_url
    response = requests.get(url)
    response.raise_for_status()
    return response.text
  
  def get_soup(self, html: str):
    return BeautifulSoup(html, "lxml")
  
  def scrape(self):
    """Método abstracto a implementar en cada scraper"""
    raise NotImplementedError("Debes implementar el método scrape()")