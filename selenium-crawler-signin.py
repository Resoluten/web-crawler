# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# 設定 Chrome Drive 的執行檔路徑
options = Options()
options.add_experimental_option("detach", True)
options.chrome_executable_path = "C:\\Users\\user\\allen\\Study_Code\\PythonSelenium\\chromedriver.exe"
# 建立 Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
# 連線到Leetcode登入頁面
driver.get("https://leetcode.com/accounts/login/")
# 輸入帳號密碼，按下登入按鈕
usernameInput = driver.find_element(By.ID, "id_login")
passwordInput = driver.find_element(By.ID, "id_password")
usernameInput.send_keys("gcobm12345@gmail.com")
passwordInput.send_keys("maericen")
# signinBtn = driver.find_element(By.XPATH, '//*[@id="signin_btn"]')
signinbtn = driver.find_element(By.ID, "signin_btn")
signinbtn.send_keys(Keys.ENTER)
# signinbtn.click()
time.sleep(5)
# 等待登入完成
# 連線到登入後才能取得資料的頁，並取得想要的資料
# driver.close()