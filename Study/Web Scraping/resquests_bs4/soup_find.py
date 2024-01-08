'''Neste exemplo, há duas formas de se fazer a requisição, mudando a forma como é 
passado os parâmetros. Uma é através do próprio find('tag', class=_'class-name', 
'class-value'), e a outra é através da chamada da função (url, tab, attribute, value).'''

import requests
from bs4 import BeautifulSoup

def get_data(url, tag, attribute, value):
# def get_data(url):
  try:
    response = requests.get(url)

    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      data = soup.find(tag, {attribute: value})
      # data = soup.find('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ dynamic-table_col-other__Eu_RC')

      if data:
        target = data.text.strip()
        return target
      else:
        print('Não foi possível encontrar o preço do produto.')
        return None
    else:
      print(f'Erro ao obter a página. Código de status: {response.status_code}')
      return None
          
  except requests.exceptions.RequestException as e:
    print(f'Erro na requisição HTTP: {e}')
    return None

def main():
  url  = 'https://br.investing.com/indices/brazil-indices'
  data = get_data(url, 'td', 'class', 'datatable_cell__LJp3C datatable_cell--align-end__qgxDQ dynamic-table_col-other__Eu_RC')
  # data = get_data(url)

  if data:
    print(f'O valor é: {data}')
  else:
    print('Não foi possível obter o preço do produto.')

if __name__ == "__main__":
  main()
