from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile")
username_field = driver.find_element(By.ID, "[username field id]")
password_field = driver.find_element(By.ID, "[password field id]")
login_button = driver.find_element(By.XPATH, "[login button xpath]")
username_field.send_No
response
generated