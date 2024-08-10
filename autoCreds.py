from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")
#chrome_options.add_argument("--headless")
driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()
print('j\'aime')
driver.get("https://www.like4like.org") 
print(driver.current_url)
time.sleep(60)

twitter_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-16y2uox r-6gpygo r-1udh08x r-1udbk01 r-3s2u2q r-peo1c r-1ps3wis r-1guathk r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]'))
twitter_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="like"]'))
tiktok_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-e2e="follow-button"]'))
instagram_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class=" _acan _acap _acas _aj1- _ap30"]'))
instagram_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81"]'))
youtube_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m"]'))
youtube_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start"]'))
facebook_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Like"], div[aria-label="Follow"], div[aria-label="Add friend"], div[aria-label="J\'aime"], div[aria-label="Suivre"]'))
pintrst_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="user-follow-button"] button'))
sndcld_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Follow"]'))


while True:
    try:
        original_window = driver.current_window_handle
        button = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id^=likebutton] a')))
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
    except Exception as e:
        continue
    
    time.sleep(5)

    try:
        follow_btn = WebDriverWait(driver, 20).until(pintrst_follow_btn)
        driver.execute_script("arguments[0].click();", follow_btn)
        time.sleep(2)
        print('task done!')
        driver.close()
    except TimeoutException:
        driver.close()
        continue
    '''follow_btn = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-e2e="follow-button"]')))
    if follow_btn:
        driver.execute_script("arguments[0].click();", follow_btn)
        time.sleep(2)'''
    time.sleep(2)
    try:
        driver.switch_to.window(original_window)
        confirm_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'pulse-checkBox')))
        driver.execute_script("arguments[0].click();", confirm_button)
    except TimeoutException:
        continue
    time.sleep(5)
    #time.sleep(100)


    

