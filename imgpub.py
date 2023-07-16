 
#! modules
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#! globals
url = "https://contributor.stock.adobe.com/hu/uploads"
pathToBrowser = "C:/Program Files/Mozilla Firefox/firefox.exe"


#! functions
def nextPage(p_driver):
    nextSpan = p_driver.find_element(By.XPATH, "//span[text()='Next']")
    nextSpan.click(); time.sleep(3)

def fillInputs(p_driver):
    # Sets category
    categoryBtn = p_driver.find_element(By.CSS_SELECTOR, '[data-t="refresh-auto-category"]')
    categoryBtn.click(); time.sleep(0.3)

    # Adds keywords
    keyWordsBtn = p_driver.find_element(By.CSS_SELECTOR, '[data-t="content-keywords-add-all-suggestions"]')
    keyWordsBtn.click(); time.sleep(0.3)

    # Sets file type
    select_element = p_driver.find_element(By.XPATH, "//select[@aria-label='File type']")
    select = Select(select_element)
    select.select_by_value("2"); time.sleep(0.3)

    # Adds title
    textarea_element = p_driver.find_element(By.CSS_SELECTOR, '[data-t="asset-title-content-tagger"]')
    textarea_element.click(); time.sleep(0.3)
    button_element = p_driver.find_element(By.XPATH, "//button[@data-t='dropdown-button']")
    button_element.click(); time.sleep(0.3)

    # Sets property
    no_span = p_driver.find_element(By.XPATH, "//span[text()='No']")
    no_span.click(); time.sleep(0.3)

def submitImages(p_driver):
    submitBtn = p_driver.find_element(By.XPATH, "//button[@data-t='submit-moderation-button']")
    submitBtn.click(); time.sleep(14)
    submitBtn = p_driver.find_element(By.XPATH, "//button[@data-t='send-moderation-button']")
    submitBtn.click(); time.sleep(12)

def jumpBackToPublishingSection(p_driver):
    newSpan = p_driver.find_element(By.XPATH, "//span[text()='New']")
    newSpan.click(); time.sleep(5)

def main():
    # Sets driver
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = pathToBrowser
    driver = webdriver.Firefox(options=firefox_options)

    # Opens target url
    driver.get(url)
    driver.implicitly_wait(20)

    while True :
        try:
            # Targets specified elements in the dom 
            imgContainerDivs = driver.find_elements(By.XPATH, '//div[@class="container-inline-block"]')
            for imgContainerDiv in imgContainerDivs:
                imgContainerDiv.click(); time.sleep(0.3)
                try:
                    fillInputs(driver)
                except Exception as e:
                    print(e)
                    continue
            submitImages(driver)
            jumpBackToPublishingSection(driver)
            # nextPage(driver)
        except Exception as e:
            print(e)


#! main
main()