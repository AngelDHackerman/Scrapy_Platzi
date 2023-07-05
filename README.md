# Scrapy_Platzi


Crear entorno virtual `python3 -m venv venv` 

Activar el entorno virtual `source venv/bin/activate` 

Una vez activado el entorno virtual, instalar las dependencias con pip3:
`pip3 install autopep8 scrapy` 


## Iniciando proyecto con scrappy

1. `scrapy startproject nombre_proyecto`
2. moverse dentro de la nueva carpeta
3. Buscar la carpeta spiders y crear el archivo para iniciar nuestro script. 

Creada la clase para iniciar scrapy, usando la variable names (previamente creada dentro de la clase)
ejecutamos el comando: `scrapy crawl <valor_dentro_de_la_variable>` e.g. __scrapy crawl quotes__


## Ejecutando La Shell de Scrapy

Para ejecutar la shell interactiva de scrappy es necesario escribir esto en consola: 
`scrapy shell 'https://DireccionWebScrappyEjemplo.com/'`

## Ejecutando los spiders de scrapy

Con esto se ejecuta el spider que creamos llamado "quotes" y que tenga un output "-o" de un archivo tipo json "quotes.json"
`scrapy crawl quotes -o quotes.json`

Es exactamente lo de arriba pero guardandolo en un archivo csv.
`scrapy crawl quotes -o quotes.csv`