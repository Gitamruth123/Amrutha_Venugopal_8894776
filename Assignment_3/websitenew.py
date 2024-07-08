# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome();
driver.get("https://flipp.com/")
time.sleep(8)

browse_link = driver.find_element("xpath","/html/body/div[5]/main/section[2]/div/a")
browse_link.click()
time.sleep(2)


dwnldapp_arrow = driver.find_element("xpath","/html/body/div[6]/flipp-listing-page/flipp-page/download-app-banner/div/button/i")
dwnldapp_arrow.click()
time.sleep(3)

latest_link = driver.find_element("xpath","/html/body/div[6]/flipp-listing-page/flipp-page/div/main/flipp-listing-page-content/div/div[1]/div/button[2]")
latest_link.click()
time.sleep(3)

shoppinglist_link = driver.find_element("xpath","/html/body/div[6]/flipp-listing-page/flipp-page/div/flipp-application-topbar/header/div/flipp-shopping-list-trigger-element/div/a/div/span[1]")
shoppinglist_link.click()
time.sleep(3)

additem_link = driver.find_element("xpath","/html/body/div[6]/flipp-shopping-list-entry/flipp-page/div/main/flipp-shopping-list-page/div/div/flipp-shopping-list/section/div[1]/flipp-shopping-item-input/flipp-searchbox/form/div/div/input[2]")
additem_link.send_keys("eggs")
time.sleep(2)
additem_link.send_keys(Keys.RETURN)
#additem_link.click()
time.sleep(3)

deals_link = driver.find_element("xpath","/html/body/div[6]/flipp-shopping-list-entry/flipp-page/div/main/flipp-shopping-list-page/div/div/flipp-shopping-list/section/div[3]/flipp-shopping-item-list/div/div[2]/ul/li/flipp-shopping-list-item/div/div[2]/div/button/div/div[2]")
deals_link.click()
time.sleep(4)

coupons_link = driver.find_element("xpath","/html/body/div[6]/flipp-shopping-list-entry/flipp-page/flipp-dialog/div/nav/div[2]/a[3]/div")
coupons_link.click()
time.sleep(3)

driver.back()
time.sleep(5)

locationchange_link = driver.find_element("xpath","/html/body/div[6]/flipp-shopping-list-entry/flipp-page/flipp-dialog/div/nav/div[2]/button/div")
locationchange_link.click()
time.sleep(2)

findflyers_link = driver.find_element("xpath","/html/body/flipp-dialog/div/form/div/button")
findflyers_link.click()
time.sleep(4)


driver.close()



