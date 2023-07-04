import sys
import time
import requests
from bs4 import BeautifulSoup


def track_price(url, target_price):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('span', class_='a-price-whole')

    if price_element is not None:
        price = price_element.text.strip().replace(',', '').replace('₹', '').replace(' ', '')
        current_price = float(price)

        if current_price < target_price:
            print("Price decreased! Book now.")

            # Perform platform-independent alert/notification
            notify_user()
        else:
            print("Price is high. Please wait for the best deal.")
    else:
        print("Price element not found.")


def notify_user():
    # Perform platform-independent alert/notification
    if sys.platform.startswith('linux'):
        # Linux notification (requires libnotify-bin package)
        title = "Price Alert"
        message = "Price decreased! Book now."
        command = f'notify-send "{title}" "{message}"'
        subprocess.call(command, shell=True)
    elif sys.platform.startswith('darwin'):
        # macOS notification
        title = "Price Alert"
        message = "Price decreased! Book now."
        command = f'display notification "{message}" with title "{title}"'
        subprocess.call(["osascript", "-e", command])
    else:
        # Default print-based notification
        print('\a')  # Emit a beep sound


def main():
    url = input("Enter the product URL: ")
    target_price = float(input("Enter your target price: "))

    while True:
        track_price(url, target_price)
        time.sleep(60)  # Track price every minute


if __name__ == "__main__":
    main()
