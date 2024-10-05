from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()  
driver.get("https://masterschool.com")
sleep(3)
browse_programs_link = driver.find_element(By.LINK_TEXT, "Browse Programs")
browse_programs_link.click()
sleep(2)
driver.quit()
