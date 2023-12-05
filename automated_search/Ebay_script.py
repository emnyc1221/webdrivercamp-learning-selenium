from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_basics.components.base import Base
from selenium_basics.components.base import assert_text
from selenium_basics.components.filter import LeftFilter

#Rolex part

driver = webdriver.Chrome()
main_page_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(main_page_url)
search_param1 = "Rolex"
search_param2 = "Casio"
page = Base(driver)
panel = LeftFilter(driver)


title_base = []
price_base = []
title_item = []
price_item = []


panel.select_option(search_param1)

for i in (0, 1):

    title_path = "//*[@class='srp-results srp-grid clearfix']/li[3]//*[@class='s-item__title']"

    price_path = "//*[@class='srp-results srp-grid clearfix']/li[3]//*[@class='s-item__price']"

    title_base.append(page.get_text(title_path))
    price_base.append(page.get_text(price_path))


    page.click((By.XPATH, title_path))


    driver.switch_to.window(driver.window_handles[i + 1])

    title_path = "//h1[@class='x-item-title__mainTitle']/span"
    price_path = "//div[@class='x-price-primary']/span"


    title_item.append(page.get_text(title_path))
    price_item.append(page.get_text(price_path))


    driver.switch_to.window(driver.window_handles[0])


for i in (0, 1):
    if not assert_text(search_param1.lower(), title_base[i].lower()):
        print(f"The option '{search_param1}' is NOT in title '{title_base[i]}'")
    if not assert_text(title_base[i], title_item[i]):
        print(f"The title on main page '{title_base[i]}' is NOT match the title on item page'{title_item[i]}'")
    if not assert_text(price_base[i], price_item[i]):
        print(f"The price on main page '{title_base[i]}' is NOT match the price on item page'{title_item[i]}'")


panel.select_option(search_param1)


#Casio part

title_base = []


panel.select_option(search_param2)

for i in (0, 1):

    title_path = "//*[@class='srp-results srp-grid clearfix']/li[63]//*[@class='s-item__title']"


    title_base.append(page.get_text(title_path))


for i in (0, 1):
    if not assert_text(search_param2.lower(), title_base[i].lower()):
        print(f"The option '{search_param2}' is NOT in title '{title_base[i]}'")


driver.quit()