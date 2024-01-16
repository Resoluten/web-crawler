# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# 設定 Chrome Drive 的執行檔路徑
options = Options()
options.chrome_executable_path = "C:\\Users\\user\\allen\\Study_Code\\PythonSelenium\\chromedriver.exe"
# 建立 Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
# 連線到 LinkenIn工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
# 捲動視窗並等待瀏覽器載入更多內容
i = 0
while i<5:
    i +=1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#捲動視窗到底部
    time.sleep(2)#等待五秒鐘
# 取得網頁中工作的標題
titleTag = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titleTags in titleTag:
    print(titleTags.text)
driver.close()