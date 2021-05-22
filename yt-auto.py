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

#
# 3つの変数を入力
# 1. URL (&t=...のない形で)
# 2. 再生開始時間
# 3. 再生終了時間
# 

url = 'https://www.youtube.com/watch?v=TZDJ3b2EAyc'
StartTime = '57:50'
EndTime = '57:58'

# xx:xx:xx形式の時間をxxxsecに変換 
def calcSec(time) -> int:
    time = time.split(':')
    if len(time) == 3:
        h, m, s = time[0], time[1], time[2]
    elif len(time) == 2:
        h, m, s = 0, time[0], time[1]

    t = 60 * 60 * int(h) + 60 * int(m) + int(s)

    return t

# 再生時間 (=プログラムの休止時間) を計算
# 入力された再生時間 + 1秒とする
def calcPlayTime() -> int:
    
    startSec = calcSec(StartTime)
    endSec = calcSec(EndTime)

    return endSec - startSec + 1

# 再生終了か判定
def whetherToFinish(currentTime, EndTime):
    currentSec = calcSec(currentTime)
    endSec = calcSec(EndTime)
    if currentSec > endSec:
        return True
    return False

# ここからメイン処理
param = calcSec(StartTime)
url = url + '&t=' + str(param) + 's'
while True:
    # urlの指定
    driver.get(url)

    # 再生時間 (=プログラムの休止時間) を指定
    playTime = calcPlayTime()
    time.sleep(playTime)

    while True:
        #ホバーしてタイマーを表示させる ※このへん渋い
        actions = ActionChains(driver)
        targetFrom = driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video')
        targetTo = driver.find_element_by_xpath('//*[@id="search"]')
        actions.click_and_hold(targetFrom)
        actions.move_to_element(targetTo)
        actions.perform()

        #時間を取得
        selector = 'ytp-time-current'
        currentTime = driver.find_element_by_class_name(selector).text

        # 再生終了か判定
        if (whetherToFinish(currentTime ,EndTime) == True):
            break
        time.sleep(3)

