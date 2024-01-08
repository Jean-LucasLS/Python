import requests
from bs4 import BeautifulSoup

# def obter_preco_produto(url, tag, attribute, value):
def get_data(url, tag):
  try:
    response = requests.get(url)
    # print(response.headers)
    
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      # data = soup.find(tag, {attribute: value})
      data = soup.select_one(tag)
      
      if data:
          target = data.text.strip()
          return target
      else:
          print("Não foi possível encontrar o preço do produto.")
          return None
    else:
      print(f"Erro ao obter a página. Código de status: {response.status_code}")
      return None
          
  except requests.exceptions.RequestException as e:
    print(f"Erro na requisição HTTP: {e}")
    return None

def main():
  url = 'https://br.investing.com/currencies/streaming-forex-rates-majors'
  
  # Ctrl + Shift + C -> Copy -> Copy selector  
  dollar_buy  = get_data(url, '#__next > div.desktop\:relative.desktop\:bg-background-default > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__LHpKS > main > div:nth-child(3) > div.dynamic-table_dynamic-table-wrapper__MhGMX > table > tbody > tr:nth-child(1) > td:nth-child(2)')
  dollar_sell = get_data(url, '#__next > div.desktop\:relative.desktop\:bg-background-default > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__LHpKS > main > div:nth-child(3) > div.dynamic-table_dynamic-table-wrapper__MhGMX > table > tbody > tr:nth-child(1) > td:nth-child(3)')

  print(f'Buying  value: {dollar_buy} US$')
  print(f'Selling value: {dollar_sell} US$')
  
if __name__ == "__main__":
    main()