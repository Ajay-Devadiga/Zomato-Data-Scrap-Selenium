from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class chromeBrowser:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--window-size=1366,768")
        self.DRIVER_PATH = './chromedriver_win32/chromedriver.exe'
        self.driver = webdriver.Chrome(options=self.options,executable_path=self.DRIVER_PATH)