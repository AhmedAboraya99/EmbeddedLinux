
    ##############################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
 
 
LOGIN_URL = 'https://www.facebook.com/login.php'
 
class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
 
 
 
    def login(self):
        email_element = self.driver.find_element(By.ID, 'email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element(By.ID, 'pass')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = self.driver.find_element(By.ID, 'loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
    
    def Msg(self,msg):
        path_element = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]') 
        path_element.click()
        time.sleep(2)
        msg_element = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]') 
        msg_element.send_keys(msg)
        post_element = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]') 
        post_element.click()
 
if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin(email='medomax90@yahoo.com', password = 'Aboraya01098Ahmed#' , browser = 'Chrome' )
    fb_login.login()

    msg = 'This is an automated post'

    fb_login.Msg(msg) 
    
    time.sleep(10)
    
    
    