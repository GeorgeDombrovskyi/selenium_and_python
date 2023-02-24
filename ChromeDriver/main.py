from selenium import webdriver
import time


browser = webdriver.Chrome(executable_path="/Users/admin/Desktop/AutoPhyton/selenium_and_phyton/ChromeDriver/chromedriver")
link = "https://rozetka.com.ua/"
try:
    browser.get(link)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()