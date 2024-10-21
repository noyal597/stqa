from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

web_page_elements = set()
web_object_elements = ['object', 'embed', 'img', 'a', 'textarea', 'audio',
                       'video', 'iframe', 'table', 'input']

driver = webdriver.Edge()
driver.get('https://www.google.com')
elements = driver.find_elements(By.XPATH, "//*")

# wait = WebDriverWait(driver, 50000)
# wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*")))

for element in elements:
    element_name = element.tag_name
    if element_name == 'input':
        element_name = element.get_attribute('type')
    if element_name in web_object_elements:
        web_page_elements.add(element_name)

print(web_page_elements)
driver.close()
