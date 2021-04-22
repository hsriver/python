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

# url = 'https://www.youtube.com/watch?v=5GiSc6BdWTE&t=2427s'
url = 'https://www.youtube.com/watch?v=5GiSc6BdWTE'
StartTime = '40:27'
EndTime = '40:40'

# 再生開始時間を計算(URLに渡すパラメータ)
def calcStartTime(StartTime):
    StartMin, StartSec = StartTime.split(':')
    t = 60 * int(StartMin) + int(StartSec)

    return t

param = calcStartTime(StartTime)
url = url + '&t=' + str(param) + 's'

print("aaaaa")
print(url)
print("aaaaa")
print(param)



# 再生時間 (=プログラムの休止時間) を計算
# 入力された再生時間 + 1秒とする
def calcPlayTime(StartTime, EndTime):
    StartMin, StartSec = StartTime.split(':')

    EndMin, EndSec = EndTime.split(':')

    MinCount = EndMin - StartMin #再生時間(分)
    SecCount = EndSec - StartSec #再生時間(秒)

    # n分m秒に変換, (0 <= m <= 59になるように)
    if (SecCount < 0):
        MinCount = MinCount - 1
        SecCount = 60 - SecCount

    return 60 * MinCount + SecCount + 1

# 再生終了か判定
def whetherToFinish(EndTime, min, sec):
    EndMin, EndSec = EndTime.split(':')

    if min >= EndMin and sec >= EndSec:
        return True
    return False

# 動画にアクセスする
while True:
    # urlの指定
    driver.get(url)

    # 再生時間 (=プログラムの休止時間) を指定
    playTime = calcPlayTime(StartTime, EndTime)
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
        currentTime = currentTime.split(':')
        min = int(currentTime[0])
        sec = int(currentTime[1])

        # 再生終了か判定
        if (whetherToFinish(EndTime, min, sec) == True):
            break
        time.sleep(3)

