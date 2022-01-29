import selenium
import os
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver


driverPath = os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver.exe')

wait = 10


class Driver:

    __instance = None

    def __init__(self):
        raise PermissionError('Initialization not allowed')

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            options = selenium.webdriver.ChromeOptions()
            #options.add_argument("--headless")
            options.add_argument("--start-maximized")
            cls.__instance = WebDriver(
                executable_path=driverPath,
                desired_capabilities=DesiredCapabilities.CHROME,
                options=options
            )
            cls.__instance.implicitly_wait(wait)
        return cls.__instance