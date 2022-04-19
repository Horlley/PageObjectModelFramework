from selenium.webdriver.common.by import By
from webdriver_manager import driver

from Utilities import configReader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, configReader.readConfig("locators", "CarTitle_XPATH")).text

    def getCarNameAndPrices(self):
        carNames: object = self.driver.find_elements(By.XPATH, configReader.readConfig("locators", "CarName_XPATH"))
        carPrices = self.driver.find_elements(By.XPATH, configReader.readConfig("locators", "CarPrice_XPATH"))

        print("Tamanho: " + str(len(carPrices)))

        for i in range(1, len(carPrices)):
            print(carNames[i].text + "----- Prices are -----" + carPrices[i].text)
