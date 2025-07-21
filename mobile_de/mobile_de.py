from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox, FirefoxOptions
import logging
import re

logger = logging.getLogger(__name__)

class URLParseFailed(Exception):
    pass

class MobileDe:
    def __init__(self, timeout: int = 10):
        self.base_url = "https://"
        self.timeout = timeout
        self.options = FirefoxOptions()
        self.options.set_preference("dom.webdriver.enabled", False)
        self.options.set_preference("useAutomationExtension", False)
        self.options.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0")
        self.options.add_argument("--headless")
        self.pattern = r"(suchen\.mobile\.de\/fahrzeuge\/details\.html\?id=\d*|suchen\.mobile\.de\/auto-inserat\/.*\/\d*\.html)"

    def html(self, url: str) -> str:
        driver = Firefox(options=self.options)
        try:
            url = self._parse_url(url)
            driver.set_window_size(1920, 1080)
            driver.get(url)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "mde-consent-modal-dialog"))
            )
            button = driver.find_element(By.CSS_SELECTOR, "[tabindex='0']")
            button.click()

            return driver.page_source
        except URLParseFailed as e:
            raise e
        except Exception as e:
            logger.error(e)
            return ""
        finally:
            driver.quit()

    def _parse_url(self, url: str) -> str:
        # https://suchen.mobile.de/fahrzeuge/details.html?id=431379188&con=NEW&dam=false&isSearchRequest=true&ref=srp&refId=4cb81ccd-09a3-e3c8-eeaa-7094b20a1f0a&s=Car&searchId=4cb81ccd-09a3-e3c8-eeaa-7094b20a1f0a&vc=Car
        # https://suchen.mobile.de/auto-inserat/mercedes-benz-vito-kombi-116-cdi-extralang-8-sitzer-klima-a-c-meschede/430458101.html
        matches = re.findall(self.pattern, url)
        if not matches:
            raise URLParseFailed
        return self.base_url + matches[0]

