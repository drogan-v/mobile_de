from mobile_de.automobile import AutoMobileFake, AutoMobile

url = "https://suchen.mobile.de/fahrzeuge/details.html?id=431347360&action=topOfPage&dam=false&isSearchRequest=true&ms=17200%3B68%3B%3B&ref=srp&refId=a849c465-ccb7-1b84-925d-ee4f47bba2ce&s=Car&searchId=a849c465-ccb7-1b84-925d-ee4f47bba2ce&vc=Car"
html_path = "tests/Mercedes-Benz.html"
automobile = AutoMobileFake(html_path)
# automobile = AutoMobile(url)

# TODO: Using urls in the tests is bad, try to make Fakes
def test_automobile_title():
    res = automobile.title()
    assert res == "Mercedes-Benz G 55 AMG"

def test_automobile_netto_price():
    res = automobile.netto_price()
    assert res == "68.554 €"

def test_automobile_brutto_price():
    res = automobile.brutto_price()
    assert res == "82.950 €"

def test_automobile_tax_vat():
    res = automobile.tax_vat()
    assert res == "21%"

def test_automobile_year_of_manufacture():
    res = automobile.year_of_manufacture()
    assert res == "2011"

def test_automobile_first_registration_date():
    res = automobile.first_registration_date()
    assert res == "02/2011"

def test_automobile_engine_capacity_cm3():
    res = automobile.engine_capacity_cm3()
    assert res == 5439
