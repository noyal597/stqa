import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
def main():
   options =Options()
   options.add_experimental_option("excludeSwitches" , ["enable-automation"])
   service = Service(r"C:\selenium\chromedriver-win64")
   driver = webdriver.Chrome(options=options ,service=service)
   url = 'https://www.instagram.com/'
   driver.get(url)
   time.sleep(1)
   email = driver.find_element(By.NAME,  'username')
   email.send_keys("vitalityvibes_auditorium")
   time.sleep(1)
   password =driver.find_element(By.NAME, "password")
   password.send_keys("instagram@1234")
   time.sleep(1)
   btn =driver.find_element(By.XPATH ,'//*[@id="loginForm"]/div/div[3]/button')
   btn.click()
   time.sleep(4000)
main()
