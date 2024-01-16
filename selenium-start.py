# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 設定 Chrome Drive 的執行檔路徑
options = Options()
options.chrome_executable_path = "C:\\Users\\user\\allen\\Study_Code\\PythonSelenium\\chromedriver.exe"
# 建立 Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot_google.jpg")
driver.get("https://www.nkust.edu.tw/")
driver.save_screenshot("screenshot_NKUST.png")
driver.close()