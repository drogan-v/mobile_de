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

    def netto_price(self) -> str:
        pass

    def brutto_price(self) -> str:
        pass

    def tax_vat(self) -> str:
        pass

    def year_of_manufacture(self) -> str:
        pass

    def mileage(self) -> str:
        pass

    def color(self) -> str:
        pass

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
        pass

    def condition(self) -> str:
        pass

    def seller(self) -> str:
        pass

    def address(self) -> str:
        pass

    def engine_type(self) -> str:
        pass

    def engine_capacity(self) -> str:
        pass

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
