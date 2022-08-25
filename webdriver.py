from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

def initializeWebDriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(100) 
    return driver

        