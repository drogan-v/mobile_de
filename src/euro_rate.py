import requests


class EuroRate:
    def __init__(self):
        self.api = "https://www.cbr-xml-daily.ru/daily_json.js"

    def euro_to_ruble(self) -> float:
        response = requests.get(self.api)
        data = response.json()

        euro_rate = data["Valute"]["EUR"]["Value"]
        return euro_rate


if __name__ == "__main__":
    e = EuroRate()
    print(e.euro_to_ruble())
