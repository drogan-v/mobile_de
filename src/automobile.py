from .mobile_de import MobileDe
from bs4 import BeautifulSoup


class AutoMobile:
    # TODO: there is a lot of functions! You can find more on the https://auto-parser.ru/parser_mobile_de
    # TODO: RELEASE ALL OF THEM
    def __init__(self, url: str):
        self.url = url
        self.html = MobileDe().html(self.url)
        self.soup = BeautifulSoup(self.html, "html.parser")

    def info(self):
        pass

    def title(self) -> str:
        return self.soup.find(class_="dNpqi").text

    def brutto_price(self) -> str:
        try:
            return self.soup.find(class_="jjvdJ").text.replace("\xa0", " ")
        except AttributeError:
            return "—"

    def netto_price(self) -> str:
        price = self.__netto_string()
        return price.split(" (Netto), ")[0].replace("\xa0", " ") if price else "—"

    def tax_vat(self) -> str:
        tax = self.__netto_string()
        return tax.split(" (Netto), ")[1].split(" ")[0] if tax else "—"

    def year_of_manufacture(self) -> str:
        element = self.soup.find("dt", attrs={"data-testid": "constructionYear-item"})
        if element:
            year = element.find_next("dd").text
            return year
        return "—"

    def mileage(self) -> str:
        element = self.soup.find("dt", attrs={"data-testid": "climatisation-item"})
        if element:
            milage = element.find_next("dd").text
            return milage
        return "—"

    def color(self) -> str:
        element = self.soup.find("dt", attrs={"data-testid": "color-item"})
        if element:
            color = element.find_next("dd").text
            return color
        return "—"

    def number_of_owners(self) -> str:
        pass

    def co2_emissions(self) -> str:
        pass

    def number_of_places(self) -> str:
        pass

    def number_of_doors(self) -> str:
        pass

    def climate_control(self) -> str:
        pass

    def autoparking(self) -> str:
        pass

    def manufacturers_color(self) -> str:
        pass

    def interior_color(self) -> str:
        pass

    def efficiency_class(self) -> str:
        pass

    def first_registration_date(self) -> str:
        element = self.soup.find("dt", attrs={"data-testid": "firstRegistration-item"})
        if element:
            date = element.find_next("dd").text
            return date
        return "—"

    def condition(self) -> str:
        pass

    def seller(self) -> str:
        pass

    def address(self) -> str:
        pass

    def engine_type(self) -> str:
        pass

    def engine_capacity_cm3(self) -> int:
        element = self.soup.find("dt", attrs={"data-testid": "cubicCapacity-item"})
        if element:
            capacity = int((element
                        .find_next("dd")
                        .text
                        .replace("\xa0", " ")
                        .split(" ")[0]
                        .replace('.', '')))
            return capacity
        return 0

    def number_of_horsepower(self) -> str:
        pass

    def body_type(self) -> str:
        pass

    def transmission_box(self) -> str:
        pass

    def seller_id(self) -> str:
        pass

    def seller_url(self) -> str:
        pass

    def seller_type(self) -> str:
        pass

    def engine_consumption(self) -> str:
        pass

    def on_the_move(self) -> str:
        pass

    def __netto_string(self) -> str:
        try:
            return self.soup.find(class_="Hr6xO").select("span.Q7YSy.ZD2EM")[0].text
        except AttributeError:
            return ""
        except IndexError:
            return ""
