import bs4 as bs
import requests
import winsound
import time

def track_price(url, target_price):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = bs.BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('span', class_='a-price-whole')
    
    if price_element is not None:
        price = price_element.text.strip().replace(',', '').replace('₹', '').replace(' ', '')
        current_price = float(price)

        if current_price < target_price:
            print("Price decreased! Book now.")
            winsound.Beep(2500, 1000)
        else:
            print("Price is high. Please wait for the best deal.")
    else:
        print("Price element not found.")

def main():
    url = input("Enter the product URL: ")
    target_price = float(input("Enter your target price: "))

    while True:
        track_price(url, target_price)
        time.sleep(60)  # Track price every minute

if __name__ == "__main__":
    main()
