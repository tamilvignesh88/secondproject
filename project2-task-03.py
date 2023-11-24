from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(30)
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])[1]").click()
driver.find_element(By.XPATH,"(//span[normalize-space()='Admin'])[1]").click()
driver.find_element(By.XPATH,"(//span[normalize-space()='PIM'])[1]").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Leave'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Time'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Recruitment'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='My Info'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Performance'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Dashboard'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Directory'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Maintenance'])[1])").click()
time.sleep(20)
driver.find_element(By.XPATH,"(//button[normalize-space()='Cancel'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Claim'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Buzz'])[1])").click()
time.sleep(30)
