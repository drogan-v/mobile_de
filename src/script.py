import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_page_html(url):
    options = FirefoxOptions()

    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0")
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    try:
        driver.set_window_size(1920, 1080)
        driver.get(url)
        print("Страница загружена")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mde-consent-modal-dialog"))
        )

        button = driver.find_element(By.CSS_SELECTOR, "[tabindex='0']")
        button.click()

        return driver.page_source

    except Exception as e:
        print(f"Ошибка: {e}")
        return None

    finally:
        driver.quit()


url = "https://suchen.mobile.de/auto-inserat/volkswagen-golf-vii-lim-gti-bmt-302ps-xenon-chemnitz/401913977.html"
html_content = get_page_html(url)

if html_content:
    with open("html.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("HTML успешно получен!")
else:
    print("Не удалось получить HTML контент")
