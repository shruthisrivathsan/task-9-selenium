from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SauceDemo:
    #initialize the class with attributes Url, username and password
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

    #create a function to open the webpage
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    #create a function to enter the credentials in the inout boxes
    def inputBox(self, value, key):
        self.driver.find_element( by = By.TAG_NAME, value = value).send_keys(key)

    #create a function to click the login button
    def loginBtn(self):
        self.driver.find_element(by= By.ID, value = "login-button").click()

    #create a function to exit the window
    def quit(self):
        self.driver.quit()

    #create a function to inout and check the credentials
    def login(self):
        self.boot()
        self.inputBox("username",self.username)
        self.inputBox("password", self.password)
        self.loginBtn()

    #create a method to get the title of the page
    def getTitle(self):
        return self.driver.title

    #create a method to get the contents of the page
    def extractContent(self):
        content = self.driver.find_element(by=By.TAG_NAME, value="body").text
        return content

    #create a method to copy the contnts of the page to a text file
    def copyContent(self):
        with open("webpage_task_11.txt", "w") as file1:
            file1.write(self.extractContent())
            
#calling the class and its obj
url = "https://www.saucedemo.com/"
obj = SauceDemo(url, username="standard_user", password="standard_user")
obj.boot()
obj.getTitle()
obj.extractContent()
obj.copyContent()
obj.quit()

