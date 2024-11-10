from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_books():
    data = []
    for i in range(1, 11):
        url = f'https://books.toscrape.com/catalogue/page-{i}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        ol = soup.find('ol')
        articles = ol.find_all('article', class_='product_pod')

        for article in articles:
            title = article.find('h3').get_text(strip=True)
            price = article.find('p', class_='price_color').get_text(strip=True)
            rating = article.find('p')['class'][1]
            in_stock = article.find('p', class_='instock availability').get_text(strip=True)
            
            data.append({"Title": title, "Price": price, "Rating": rating, "Availability": in_stock})
    
    df = pd.DataFrame(data)
    return df.to_dict(orient='records')
