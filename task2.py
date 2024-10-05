from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("cats")
sleep(3)
print(driver.title)
driver.quit()
