import pdfplumber
import json

#LOAD PDF
with open("towns.json") as f:
    towns = json.load(f)

town_names = [t["name"] for t in towns]

#READ LINES IN A TOWN'S NAME
lines = []
with pdfplumber.open("contacts.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            for line in text.split("\n"):
                lines.append(line.strip())

#MATCH EACH LINE TO A TOWN NAME
towns_emails = {}
for line in lines:
    if "@" not in line:
        continue
    for town in town_names:
        if line.startswith(town):
            email = line.split()[-1].lower()
            towns_emails[town] = email
            break

print(f"Matched {len(towns_emails)} towns with emails")
missing = [t for t in town_names if t not in towns_emails]
print(f"Missing {len(missing)}:")
for t in missing:
    print(t)

print("\nRaw lines for missing towns:")
for line in lines:
    for town in missing:
        if town.split()[0] in line:
            print(repr(line))

#OUTPUT
output = []
for town in towns:
    entry = {
        "name": town["name"],
        "website": town["website"],
        "email": towns_emails.get(town["name"], "")
    }
    output.append(entry)

with open("targets.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Saved {len(output)} towns to targets.json")
