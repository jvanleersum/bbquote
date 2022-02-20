import requests

def get_quote():
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    response = requests.get(url).json()
    quote = response[0]["quote"]
    author = response[0]["author"]
    return quote

if __name__ == "__main__":
    print(get_quote())