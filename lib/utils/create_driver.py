import pytest
from selenium.webdriver import Chrome,Ie,edge

def get_driver_instance():
    browser=pytest.config.option.type.lower()
    if browser == "chrome":
        driver = Chrome("./browser-server/chromedriver.exe")

    if browser == "ie":
        driver = Ie("./browser-server/IEDriverServer.exe")

    if browser == "edge":
        driver = edge("./browser-server/MicrosoftWebDriver.exe")

    else:
        print("Invalid Browser Option")
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://localhost")
    return driver
