from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

#
# Seleniumをあらゆる環境で起動させるChromeオプション
#
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')

options = webdriver.ChromeOptions()
profile_path = '/Users/takum/AppData/Local/Google/Chrome/User Data'
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument('--profile-directory=Default')
#options.add_argument('--start-maximized')
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

#
# Chrome ドライバーの起動
#
DRIVER_PATH = '/Users/takum/Selenium/chromedriver'
# DRIVER_PATH = '/Users/Kenta/Desktop/Selenium/chromedriver' # ローカル

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

# 動画にアクセスする
while True:
    # urlの指定
    url = 'https://www.youtube.com/watch?v=5GiSc6BdWTE&t=2427s'
    driver.get(url)

    time.sleep(5)
    while True:
        #ホバーしてタイマーを表示させる
        driver_action = ActionChains(driver)
        driver_action.move_to_element(driver.find_element_by_xpath('//*[@id="movie_player"]')).perform()

        #時間を取得
        selector = 'ytp-time-current'
        currentTime = driver.find_element_by_class_name(selector).text
        currentTime = currentTime.split(':')
        print(currentTime)
        print(currentTime[0])
        print(currentTime[1])
        #min = int(currentTime[0])
        #sec = int(currentTime[1])

        #print(min + " and ")
        #print(sec)

        # if min >= 44 and sec >= 40:
            # break

        # time.sleep(2)
        break





