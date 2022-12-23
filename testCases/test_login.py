import pytest
import time
from selenium import webdriver
from pageObjects.Loginpage import login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getUserPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**************Test_001_Login****************")
        self.logger.info("**************Homepage Verify title****************")
        #
        #self.driver=webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver=setup
        self.driver.get(self.baseURL)
        #time.sleep(5)
        act_title=self.driver.title
       # self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************HomePage_Title_Is_Passed****************")
            #
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************HomePage_Title_Is_Failed****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************Verifying_the_login_test**************")
        #self.driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver_win32\chromedriver.exe")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=login(self.driver)     # inhereting the class method
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        #self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************login_test_is_passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("**************Login_Test_Is_failed**************")
            self.driver.close()
            assert False




