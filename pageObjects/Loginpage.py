from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login:
    username="Email"
    password="Password"
    login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logout_link="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)

    def setPasword(self,password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)

    def clickLogin(self):
        #self.driver.find_e(self.password).clear()
        self.driver.find_element(By.XPATH,self.login_xpath).click()
        time.sleep(5)

    def clickLogout(self):
        #self.driver.find_e(self.password).clear()
        self.driver.find_element(By.LINK_TEXT,self.logout_link).click()
        time.sleep(2)

    def setPassword(self, password):
        pass