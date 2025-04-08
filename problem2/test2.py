from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://agrichain.com")

input_box = driver.find_element(By.ID, "input")
input_box.send_keys("abcabcbb")

submit_btn = driver.find_element(By.CLASS_NAME, "submitbtn")
submit_btn.click()

wait = WebDriverWait(driver, 10)
result_element = wait.until(EC.presence_of_element_located((By.ID, "result")))

expected_result = "abc"
actual_result = result_element.text
assert expected_result == actual_result

driver.close()
