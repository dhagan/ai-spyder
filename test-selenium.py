from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def search(driver, address):
    #driver = webdriver.Chrome('./chromedriver')
    print(driver.title)
    time.sleep(5)
    search_bar = driver.find_element(By.ID,"esri_dijit_Search_0_input")
    search_bar.clear()
    search_bar.send_keys(address)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    items = driver.find_elements(By.CLASS_NAME,"esriCTItemlList")
    print(items[0].text)
    items[0].click()
    ele=driver.find_element(By.XPATH, "//td[contains(text(),'@capitol.hawaii.gov')]")
    return ele.text
    
    # for item in items:
    #     print(item.text)
    #     if item.text == '':
    #         print('empty item')
    #         continue
    #     time.sleep(10)
    #     item.click()
    #     ele=driver.find_element(By.XPATH, "//td[contains(text(),'@capitol.hawaii.gov')]")
    #     if ele.text == '':
    #         item.click()
    #         ele=driver.find_element(By.XPATH, "//td[contains(text(),'@capitol.hawaii.gov')]")
    #     #print(ele)
    #     if 'sen' in ele.text :
    #         senatorInfo = ele.text
    #         driver.find_element(By.XPATH,"//div[@title='Senate Districts']").click()
    #         #driver.find_element(By.CLASS_NAME,"esriCTLastLayerFocusNode").click()
    #     elif 'rep' in ele.text : 
    #         representativeInfo = ele.text
    #         break
    #     #popup = driver.find_elements(By.ID,"esri_dijit__PopupRenderer_0")
    #     # popup = driver.find_elements(By.CLASS_NAME,"esriViewPopup")
    #     # print(popup[0].text)
    #     # if  'Senator' in popup[0].text :
    #     #     senatorInfo = popup[0].text
    #     # else : 
    #     #     representativeInfo = popup[0].text
    #     ##driver.find_element(By.CLASS_NAME,"esriCTItemLeftArrow").click()
    #     #item.click()
       

    # return {
    #     "senator" : senatorInfo, "representative" : representativeInfo
    # }

def get_by_address(address) :
    driver = webdriver.Chrome()
    driver.get("https://www.capitol.hawaii.gov/fyl/")
    info = search(driver, address)
    driver.close()
    return info


def get_all() :
    address = "123 Main St, Honolulu, HI"
    info = get_by_address(address)
    print (info)
    address = "22 Hoku Place, Paia HI 96779"
    info = get_by_address(address)
    print (info)

get_all()