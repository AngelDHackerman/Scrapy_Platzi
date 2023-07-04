import scrapy

class QuotesSpider(scrapy.Spider):
  # Nombre del spider: 
  name = 'quotes'

  # URL donde el spider hara scraping: 
  start_urls = [
    'https://quotes.toscrape.com/'
  ]
  
  # response, contiene toda la informacion de la pagina web que se ha descargado.
  def parse (self, response):
    with open('resultados.html', 'w', encoding='utf-8') as f:
      # Escibiendo el contenido de "response" en el archivo "resultados.html"
      f.write(response.text)