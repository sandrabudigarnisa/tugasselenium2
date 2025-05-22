from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://booking.kai.id/')

driver.find_element (By.ID, 'origination-flexdatalist').send_keys('PASARSENEN')
driver.find_element (By.XPATH, '//*[@id="origination-flexdatalist-results"]/li[2]/span[2]').click()

driver.find_element (By.ID, 'destination-flexdatalist').send_keys('GARUT')
driver.find_element (By.XPATH, '//*[@id="destination-flexdatalist-results"]/li[2]/span[2]').click()

# Pilih tanggal keberangkatan 
tanggal_input = driver.find_element(By.ID, "departure_dateh")
tanggal_input.click()

try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'ui-datepicker-div')))
    holiday = driver.find_elements(By.XPATH, '//td[@class=" holiday"]')
    holiday[0].click()
except TimeoutException:
    pass

driver.find_element (By.ID, 'submit').click()