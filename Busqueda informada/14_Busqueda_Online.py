
import requests
from bs4 import BeautifulSoup
def busqueda_online (duda):
    linkL = f'https://www.google.com/search?q={duda}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    try:
        page = requests.get(linkL, headers=headers)
        page.raise_for_status()
        soup = BeautifulSoup(page.text, 'html.parser')
        resultados = soup.find_all('h3')
        for i, resultado in enumerate (resultados,1):
            print(f'{i}.{resultado.get_text()}')

    except requests.exceptions as e :
        print(f'Error de conexion {e}')
    except Exception as e:
        print(f'ahi problemas{e}')
        
if __name__ == 'main':
    busqeuda = input('que tema desea buscar : ')
    busqueda_online(busqeuda)
                                          
