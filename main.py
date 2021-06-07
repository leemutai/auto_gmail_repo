from selenium import webdriver
import  time
from selenium.webdriver.common.keys import Keys
#open google chrome browser
driver = webdriver.Chrome()
#maximize the window size
driver.maximize_window()
#delete the cookies
driver.delete_all_cookies()
#navigate to yhe url
driver.get("https://www.gmail.com")
#identify the user name text box and enter the value
driver.find_element_by_id("identifierId").send_keys("youremailhere").time.sleep(2)
#click on the next button
driver.find_element_by_xpath('//*[@id=identifierNext"/div/button/div[2]').click()time.sleep(3)
#identify the password text box and enter the value
driver.find_element_by_name("password").send_keys("########")time.sleep(3)