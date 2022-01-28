"""
    WebScraping con Beautiful Soup sacando todos los títulos de las noticias de elpais.com
        ******---> https://jarroba.com/scraping-python-beautifulsoup-ejemplos/
"""

from bs4 import BeautifulSoup
import requests

url = "https://elpais.com/"

# Realizamos la peticion a la web
peticion = requests.get(url)
# print(peticion) #<Response [200]>

# Comprobamos que la peticion nos devuelve el estado del codigo = 200
#   (el codigo 200 indica que la peticion ha tenido exito)
estadoCodigo = peticion.status_code
# print(estadoCodigo) #200

if estadoCodigo == 200:
    # Pasamos el contenido web a un objeto BeautifulSoup() que convertimos a tipo texto, es decir, tenemos el
    #   codigo html en formato texto y podemos imprimirlo por pantalla.
    html = BeautifulSoup(peticion.text, "html.parser")
    # print(html) #Imprime todo el codigo html.

    # Obtenemos las partes del html donde estan los articulos, en especial sus titulares, mirando el codigo html
    #   estos titulares se encuentran en la etiqueta header y con la clase c_h.
    titulares = html.find_all('header',{'class':'c_h'})
    # print(titulares) #Imprime todo el contenido de las etiquetas header en formato html.

    # Recorremos las cabeceras para extraer los datos que nos interesan unicamente y no todo el codigo completo de
    #   la cabecera (header).
    for i, titular in enumerate(titulares):
        # con find buscamos todos los enlaces del html y devolvemos su salida en modo texto con getText(), si no
        #   hacemos la conversion a texto, nos devuelve todo el codigo html.
        noticia = titular.find('a').getText()

        print(noticia)

else:
    print("No se ha alcanzado la peticion y devuelve el código: %d" %estadoCodigo)