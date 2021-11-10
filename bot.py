from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#https://sites.google.com/chromium.org/driver/  THIS IS THE LINK TO DOWNLOAD THE WEBDRIVERS FOR YOUR CHROME BROWSER

PATH = "path"#GET THE PATH TO THE WEBDRIVER YOU JUST DOWNLOADED


driver = webdriver.Chrome(PATH)
msg = ""#ENTER A MESSAGE YOU WAN TO SEN
name  = ""#ENTER THE NAME OF THE PARSON YOU WANT TO SEARCH FOR
driver.get("https://web.whatsapp.com/")#website path you want to go to

print("PRESS ENTER")
input()
print("LOGGED IN")

time.sleep(5)#PAUSE FOR 5 SECONDS

search = driver.find_element_by_xpath("")#GET THE HTML TAG/XPATH OF THE SEARCH BAR
search.send_keys(name)
search.send_keys(Keys.ENTER)#CLICK ENTER AFTER ENTERING TEXT IN THE SEARCH BAR

message = driver.find_element_by_xpath("")#GET THE HTML TAG/XPATH OF THE INPUT BOX

message.send_keys(msg)
message.send_keys(Keys.ENTER)#CLICK ENTER AFTER ENTERING TEXT IN THE SEARCH BAR

time.sleep(10)#PAUSE FOR 6 SECONDS
driver.quit()#close the entire browser