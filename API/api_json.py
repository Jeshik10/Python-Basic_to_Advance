import requests
import json

url = "https://jsonguide.technologychannel.org/quotes.json"
response = requests.get(url)
quotes = json.loads(response.text)

for index, quote in enumerate(quotes, start=1):
    # Strip quotation marks from the beginning and end of each quote
    clean_quote = quote["text"].strip('"')
    print(f"{index}. {clean_quote}")