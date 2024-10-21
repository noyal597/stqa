from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("http://127.0.0.1:5000")
select = driver.find_element(By.ID,"mycombo")
options=select.find_elements(By.TAG_NAME,"option")
for option in options:
    print(option.text + "-" + option.get_attribute('value'))
driver.quit()