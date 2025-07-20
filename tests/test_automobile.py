from src.automobile import AutoMobile


# TODO: Using urls in the tests is bad, try to make Fakes
def test_automobile_name():
    link = "https://suchen.mobile.de/fahrzeuge/details.html?id=431379188&con=NEW&dam=false&isSearchRequest=true&ref=srp&refId=4cb81ccd-09a3-e3c8-eeaa-7094b20a1f0a&s=Car&searchId=4cb81ccd-09a3-e3c8-eeaa-7094b20a1f0a&vc=Car"
    automobile = AutoMobile(link)
    res = automobile.title()
    assert res == "Volkswagen Golf"
