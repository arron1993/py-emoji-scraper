import requests
import pyquery
import json

CATEGORIES = [
        "people", "nature", "food-drink",
        "activity", "travel-places", "objects",
        "symbols", "flags"]

def main():
    results = {}
    for category in CATEGORIES:
        url = f"https://emojipedia.org/{category}/"
        page = pyquery.PyQuery(requests.get(url).content)
        emojies = [emoji.text for emoji in page.find(".emoji-list .emoji")]
        results[category] = emojies

    with open("./emojis.json", 'w') as f:
        f.write(json.dumps(results))

    return 0

if __name__ == "__main__":
    main()