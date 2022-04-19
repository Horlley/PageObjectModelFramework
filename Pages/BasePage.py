from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import configReader
import logging

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_TAG"):
            self.driver.find_element(By.TAG_NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_LINK"):
            self.driver.find_element(By.LINK_TEXT, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_LINKP"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicando no elemento: " + str(locator))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_TAG"):
            self.driver.find_element(By.TAG_NAME, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASS"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_LINK"):
            self.driver.find_element(By.LINK_TEXT, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_LINKP"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, configReader.readConfig("locators", locator)).send_keys(
                value)
        log.logger.info("Tipo de elemento: " + str(locator) + " Valor de entrada: " + str(value))

    def select(self, locator, value):
        global dropdow
        if str(locator).endswith("_XPATH"):
            dropdow = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdow = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdow = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        select = Select(dropdow)
        select.select_by_visible_text(value)

        log.logger.info("Selecionado um elemento: " + str(locator) + " Valor selecionado: " + str(value))

    def moveTo(self, locator):

        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Movel para o elemento: " + str(locator))
