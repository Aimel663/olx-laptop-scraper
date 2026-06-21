import requests
from bs4 import BeautifulSoup

def scrape_olx_laptops():
    url = "https://www.olx.com.pk/laptops-c1453"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    laptops = soup.find_all('li', class_='_3nWPz')
    
    print("OLX Laptop Prices:\n")
    for i, laptop in enumerate(laptops[:10], 1):
        try:
            title = laptop.find('span', class_='_2gr10').text.strip()
            price = laptop.find('span', class_='_89yzn').text.strip()
            print(f"{i}. {title} - {price}")
        except:
            continue

if __name__ == "__main__":
    scrape_olx_laptops()
