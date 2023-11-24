from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import  time

driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)

#driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"(//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header'])[1]").click()
driver.find_element(By.XPATH,"(//input[@placeholder='Username'])[1]").send_keys("Admin")
driver.find_element(By.XPATH,"(//button[normalize-space()='Reset Password'])[1]").click()
time.sleep(60)

