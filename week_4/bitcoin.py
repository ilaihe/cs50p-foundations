import sys
import requests

API_KEY = "YOUR_ACTUAL_API_KEY_HERE"


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=12a41cc1bf922465cbe12ae0c55318c9203c801794455e8d9ddbd4af82b6574d"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request error")

    total = bitcoins * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
