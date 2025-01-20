from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://freelance-learn-automation.vercel.app/login")
driver.find_element(By.XPATH,"//button[text()='Sign in']").click()
Errormessage = driver.find_element(By.XPATH,"//*[contains(text(),'Email')]").is_displayed()
if Errormessage == True:
    print("Pass")
else:
    print("Fail")