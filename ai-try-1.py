from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_senator_or_representative(address):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.capitol.hawaii.gov/fyl")

    # Find and fill the address input field
    address_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "address"))
    )
    address_input.send_keys(address)

    # Click the search button
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
    )

    # Get the senator or representative information
    senator_or_representative = driver.find_element(By.CLASS_NAME, "search-results").text

    # Close the browser
    driver.quit()

    return senator_or_representative

# Example usage
address = "123 Main St, Honolulu, HI"
result = get_senator_or_representative(address)
print(result)
