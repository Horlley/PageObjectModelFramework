import pytest
from Pages.RegistrationPage import RegistrationPage
from Testscases.BaseTest import Basetest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_doSignUp(Basetest):
    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password",
                             dataProvider.get_data("LoginTest"))
    def test_doSignUp(self, name, phoneNum, email, country, city, username, password):
        log.logger.info("Teste inicializado")
        regPage = RegistrationPage(self.driver)
        regPage.fillForm(self, name, phoneNum, email, country, city, username, password)
        log.logger.info("Teste de cadastro executado com sucesso")
