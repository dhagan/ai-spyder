from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium driver
driver = webdriver.Chrome()

# Open the website
driver.get('https://www.capitol.hawaii.gov/fyl')

# Find the address input field and enter the address
address_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
address_input.send_keys('123 Main Street, Honolulu, HI')

# Find the search button and click it
search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchButton')))
search_button.click()

# Wait for the results to load
results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'results')))

# Extract the Senator and Representative information
senator = results.find_element(By.XPATH, '//div[@id="results"]/div[1]/div[2]/div[1]/div[2]').text
representative = results.find_element(By.XPATH, '//div[@id="results"]/div[1]/div[2]/div[2]/div[2]').text

# Print the Senator and Representative information
print('Senator:', senator)
print('Representative:', representative)

# Close the browser
driver.quit()