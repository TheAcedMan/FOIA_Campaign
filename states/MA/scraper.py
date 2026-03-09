import requests
from bs4 import BeautifulSoup
import json

url = "https://www.mass.gov/lists/massachusetts-city-and-town-websites"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

towns = []

for div in soup.find_all("div", class_="ma__download-link"):
    a_tag = div.find("a")
    span_tag = div.find("span", class_=False)
    
    if a_tag and span_tag:
        name = span_tag.text.strip()
        link = a_tag["href"]
        towns.append({"name": name, "website": link})

for town in towns[:5]:
    print(town)

print(f"\nTotal towns found: {len(towns)}")

with open("towns.json", "w") as f:
    json.dump(towns, f, indent=2)

print("Saved to states/MA/towns.json")
