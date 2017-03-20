from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
baseurl = "http://google.ie"


mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()


mydriver.find_element_by_xpath(".//*[@id='gs_htif0']").send_keys("weather dublin")
time.sleep(5)
#Clear Password TextBox if already allowed "Remember Me" 
wind_info = mydriver.find_element_by_xpath(".//*[@id='wob_ws']")
print wind_info.text

