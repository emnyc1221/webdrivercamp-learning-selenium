from selenium import webdriver
from components.filter import LeftFilter

driver = webdriver.Chrome
left_filter = LeftFilter(driver)

# Print the list of available attributes and methods of the object
print(dir(left_filter))
