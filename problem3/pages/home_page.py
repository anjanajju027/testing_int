from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def _init_(self, driver):
        self.driver = driver
        self.input_id = (By.ID, "input")
        self.submit_class = (By.CLASS_NAME, "submitbtn")
        self.result_id = (By.ID, "result")

    def enter_input(self, text):
        self.driver.find_element(*self.input_id).send_keys(text)

    def click_submit(self):
        self.driver.find_element(*self.submit_class).click()

    def get_result(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.result_id)).text
    