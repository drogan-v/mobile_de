# Mobile DE
Library for getting basic information about cars from the website suchen.mobile.de

## Installing
```bash
pip install git+https://github.com/drogan-v/mobile_de.git
```

## Usage

```python
from mobile_de import AutoMobile

url = "<url to car>"
automobile = AutoMobile(url)
print(automobile.title())
```
## Testing
There is two classes in the project: `AutoMobile` и `AutoMobileFake`. The tests are located in the /tests directory. 
They can work with either of the two classes. If you want to run quick unit tests, you should download webpage from mobile.de.
Example of the html file for tests:
- https://limewire.com/d/zxoLG#CoSFTwHhSL

If you want to run slow integration tests, you should uncomment the last line in the test_automobile.py:
```python
from mobile_de.automobile import AutoMobileFake, AutoMobile

url = "https://suchen.mobile.de/fahrzeuge/details.html?id=431347360&action=topOfPage&dam=false&isSearchRequest=true&ms=17200%3B68%3B%3B&ref=srp&refId=a849c465-ccb7-1b84-925d-ee4f47bba2ce&s=Car&searchId=a849c465-ccb7-1b84-925d-ee4f47bba2ce&vc=Car"
html_path = "tests/Mercedes-Benz.html"
automobile = AutoMobileFake(html_path)
# automobile = AutoMobile(url) # <-- uncomment this line
```
