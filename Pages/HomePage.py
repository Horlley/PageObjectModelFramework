import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.click("idioma_XPATH")
        time.sleep(1)
        self.moveTo("newCar_XPATH")
        self.click("findNewCars_XPATH")

        return NewCarsPage(self.driver)

    def gotoCampareCars(self):
        pass

    def gotoUsedCars(self):
        pass
