import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape product details
def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Send HTTP request to the provided URL
    page = requests.get(url, headers=headers)

    # Create a BeautifulSoup object and parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Lists to store product information
    products = []
    prices = []
    ratings = []

    # Find all product listings on the page
    for item in soup.find_all('div', class_='s-main-slot s-result-list s-search-results sg-row'):

        # Scrape product name
        for name in item.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
            products.append(name.text)

        # Scrape product price
        for price in item.find_all('span', class_='a-price-whole'):
            prices.append(price.text)

        # Scrape product rating
        for rating in item.find_all('span', class_='a-icon-alt'):
            ratings.append(rating.text)

    # Zip the data together into rows
    data = zip(products, prices, ratings)

    # Save data to CSV
    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating"])
        writer.writerows(data)

    print("Scraping completed and data saved to products.csv")

# URL of the e-commerce page to scrape (Amazon's product page)
url = 'https://www.amazon.com/s?k=laptops'

if __name__ == "__main__":
    scrape_amazon(url)
