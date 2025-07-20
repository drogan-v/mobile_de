from src.mobile_de import MobileDe

def test_links():
    # It's a fragile test, but it's needed to verify that the link is parsed correctly.
    links = [
        "https://suchen.mobile.de/fahrzeuge/details.html?id=431379188&con=NEW&dam=false&isSearchRequest=true&ref=srp&refId=4cb81ccd-09a3-e3c8-eeaa-7094b20a1f0a&s=Car&searchId=4cb81ccd-09a3-e3c8-eeaa-7094b20a1f0a&vc=Car",
        "https://suchen.mobile.de/auto-inserat/volkswagen-golf-vii-lim-gti-bmt-302ps-xenon-chemnitz/401913977.html"
    ]
    assert MobileDe()._parse_url(links[0]) == "https://suchen.mobile.de/fahrzeuge/details.html?id=431379188"
    assert MobileDe()._parse_url(links[1]) == "https://suchen.mobile.de/auto-inserat/volkswagen-golf-vii-lim-gti-bmt-302ps-xenon-chemnitz/401913977.html"
