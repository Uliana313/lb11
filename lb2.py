import json

drives = [
    {
        "brand": "Drive1",
        "capacity_gb": 500,
        "price_usd": 50
    },
    {
        "brand": "Drive2",
        "capacity_gb": 1000,
        "price_usd": 85
    },
    {
        "brand": "Drive3",
        "capacity_gb": 750,
        "price_usd": 70
    }
]

with open('drives.json', 'w') as json_file:
    json.dump(drives, json_file, indent=4)

print("Дані збережено у файл drives.json")
