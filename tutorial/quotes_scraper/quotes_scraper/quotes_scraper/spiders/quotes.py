import scrapy

# Título = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]//li[@class="next"]/a/@href


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # Nombre del spider
    start_urls = [
        'http://quotes.toscrape.com/page/1/'  # URL inicial para comenzar el scraping
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',  # Nombre del archivo donde se guardarán los resultados
        'FEED_FORMAT': 'json',  # Formato del archivo de salida
        'CONCURRENT_REQUESTS': 24, # numero de request que mandara al mismo tiempo
        'MEMUSAGE_LIMIT_MB': 2048,  # cantidad de ram que el scraper puede usar. 
        'MEMUSAGE_NOTIFY_MAIL': ['angel@testing.com'],  # A este correo sera enviado un mensaje si el uso de memeoria se sobrepasa
        'ROBOTSTXT_OBEY': True,  # Indica que tiene que obedecer el documento robots.txt de la pagina web. 
        'FEED_EXPORT_ENCODING': 'utf-8', # Formato de lectura, (aceptar caracteres del alfabeto español)
    }

    def parse_only_quotes(self, response, **kwargs):
        # Esta función se encarga de extraer solo las citas de la página
        if kwargs:
            quotes = kwargs['quotes']
        # Extrae las citas de la página actual
        quote_blocks = response.xpath('//div[@class="quote"]')
        for quote in quote_blocks:
            text = quote.xpath('.//span[@class="text" and @itemprop="text"]/text()').get()
            author = quote.xpath('.//span/small[@class="author" and @itemprop="author"]/text()').get()
            quotes.append({
                'text': text,
                'author': author
            })

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()  # Busca el enlace al botón de la siguiente página
        if next_page_button_link:
            # Si encuentra el enlace, sigue el enlace y llama a la misma función para la siguiente página
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            # Si no encuentra el enlace (es decir, estamos en la última página), devuelve las citas que ha recopilado
            yield {
                'quotes': quotes
            }


    def parse(self, response):
        # Esta función se encarga de extraer el título de la página y los tags principales
        # Extrae el título de la página
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()  # Extrae las citas de la página
        # Extrae los tags principales
        top_tags = response.xpath(
            '//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()

        # Indicando cuantos top tags queremos traer, en consola se ejecuta: scrapy crawl quotes -a top=3
        # Obtiene el número de tags principales que el usuario quiere extraer
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            # Si el usuario especificó un número, solo extrae esa cantidad de tags
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_tags': top_tags  # Devuelve el título de la página y los tags principales
        }

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()  # Busca el enlace al botón de la siguiente página
        if next_page_button_link:
            # Si encuentra el enlace, sigue el enlace y llama a la función parse_only_quotes para la siguiente página
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
