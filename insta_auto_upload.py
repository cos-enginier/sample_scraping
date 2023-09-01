import time
# WebDriverライブラリをインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# ChromeのWebDriverライブラリをインポート
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#ユーザ/パスワード
username = ""
password = ""
#写真のパス
media_path = ''

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10) # ページ読み込み最大待ち時間
driver.get("https://www.instagram.com/")

#ウインドサイズの指定
driver.set_window_size(1050,700)

#ユーザ/パスワード
driver.find_element(By.NAME,"username").click()
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME,"password").click()
driver.find_element(By.NAME,"password").send_keys(password)
#ログインボタン
driver.find_element(By.CSS_SELECTOR,".\\_acap").click()

#ログイン情報の保存/後で選択
element=driver.find_element(By.CSS_SELECTOR,".\\_acap")
actions=ActionChains(driver)
actions.move_to_element(element).perform()
element=driver.find_element(By.CSS_SELECTOR,"body")
actions=ActionChains(driver)
#お知らせをオン/後で選択
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR,".xjqpnuy").click()
driver.find_element(By.CSS_SELECTOR,".\\_a9_1").click()

#新規投稿をクリック
driver.find_element(By.XPATH,'//*[@aria-label="新規投稿"]').click()
time.sleep(3)
#ファイル選択
upload_input = driver.find_element_by_xpath('//input[@type="file"]')
upload_input.send_keys(media_path)
time.sleep(3)

#次へを2回押す
for i in range(2): 
    driver.find_element(By.XPATH,'//*[@role="button" and contains(text(), "次へ")]').click()
    time.sleep(3)

#シェアボタン押下
driver.find_element(By.XPATH,'//*[@role="button" and contains(text(), "シェア")]').click()
time.sleep(5)

#投稿画面を閉じる
driver.find_element(By.XPATH,'//*[@aria-label="閉じる"]').click()
time.sleep(5)

# 画面を閉じる
driver.quit()
