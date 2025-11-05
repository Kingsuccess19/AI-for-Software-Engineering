from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid credentials
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "loginBtn").click()

assert "Dashboard" in driver.title

# Invalid credentials
driver.find_element(By.ID, "username").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "loginBtn").click()

assert "Invalid" in driver.page_source
driver.quit()
