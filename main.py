import json

new_data = []
with open('reports/forbes.json', 'r') as forbes, open('reports/companies.json', 'r') as nasdaq:
    forbes_data = json.load(forbes)
    nasdaq_data = json.load(nasdaq)
    for company_forbes in forbes_data:
        for company_nasdaq in nasdaq_data:
            if company_forbes["name"] in company_nasdaq["name"]:
                new_item = {
                    "rank": company_forbes["rank"],
                    "name": company_forbes["name"],
                    "link": company_nasdaq["url"],
                }
                new_data.append(new_item)
                break

print(new_data)

with open('reports/nasdaq_companies.json', 'w') as file:
    json.dump(new_data, file, indent=4)
