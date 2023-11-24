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
expected_title = "OrangeHRM"
time.sleep(20)

driver.find_element(By.XPATH,"(//span[normalize-space()='Admin'])[1]").click()
try:
        WebDriverWait(driver, 10).until(EC.title_contains(expected_title))
        print(f"Page title is '{expected_title}'. Validation passed!")
except TimeoutException:
        print(f"Page title is not '{expected_title}'. Validation failed.")  
driver.find_element(By.XPATH,"((//span[normalize-space()='User Management'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Job'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Organization'])[1])").click()
driver.find_element(By.XPATH,"((//span[normalize-space()='Qualifications'])[1])").click()
driver.find_element(By.XPATH,"((//a[normalize-space()='Nationalities'])[1])").click()
time.sleep(10)
driver.find_element(By.XPATH,"((//a[normalize-space()='Corporate Branding'])[1])").click()
time.sleep(10)
driver.find_element(By.XPATH,"((//span[normalize-space()='Configuration'])[1])").click()
time.sleep(30)
