#
# 백준(Baekjoon Online Judgement)의 2022 만우절 강화 이벤트를 자동으로 시도합니다.
# 1. 파괴 방지 강화를 우선적으로 적용합니다.
# 2. 파괴방지 강화가 없는 경우, 강화를 시도합니다.
#
# 작성자는 결국 포인트를 모두 날렸습니다.
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time

path = "chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://solved.ac/login?prev=%2Fevent%2F220401")

while True:
    WebDriverWait(driver, sys.maxsize).until(lambda driver: driver.current_url == "https://solved.ac/event/220401")
    normal_up = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div[3]/div[1]/div/button[1]")
    power_up = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div[3]/div[1]/div/button[2]")

    # 파괴 방지 강화가 가능하다면, 우선적으로 적용한다.
    if power_up.is_enabled():
        power_up.click()
        print("파괴 방지 강화!")
        time.sleep(1)
    else:
        normal_up.click()
        print("강화!")
        time.sleep(1)
