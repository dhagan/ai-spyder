from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver.get("http://www.example.com") #This is a dummy website URL
driver.get("https://www.capitol.hawaii.gov/fyl/")
try:
    search_bar = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "esri_dijit_Search_0_input")) #This is a dummy element
    )
    #search_bar = driver.find_element(By.ID,"esri_dijit_Search_0_input")
    search_bar.clear()
    search_bar.send_keys("22 Hoku Place, Paia HI 96779")
    search_bar.send_keys(Keys.RETURN)
finally:
    driver.quit()