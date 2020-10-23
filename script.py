from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#
# Seleniumをあらゆる環境で起動させるChromeオプション
#
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す


#
# Chrome ドライバーの起動
#
DRIVER_PATH = '/Users/takum/Selenium/chromedriver'
# DRIVER_PATH = '/Users/Kenta/Desktop/Selenium/chromedriver' # ローカル

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

# Webページにアクセスする
url = 'https://google.com/'
driver.get(url)

# 検索窓にSeleniumと入力する
selector = '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
element = driver.find_element_by_css_selector(selector)
element.send_keys('Selenium')

# enterキーを押す
element.send_keys(Keys.ENTER)

# 1位の記事のタイトルを取得する
selector = '#rso > div > div:nth-child(1) > div > a > h3 > span'
element = driver.find_element_by_css_selector(selector)
page_title = element.text

# 1位の記事のURLを取得する
selector = '#rso > div > div:nth-child(1) > div > a'
element = driver.find_element_by_css_selector(selector)
page_url = element.get_attribute('href')

# ブラウザを終了する(全てのウィンドウを閉じる）
# Chromeのショートカットキー(Command+Q)と同じ動作
driver.quit()

print(page_title, page_url)