from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")
driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()

twitter_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-16y2uox r-6gpygo r-1udh08x r-1udbk01 r-3s2u2q r-peo1c r-1ps3wis r-1guathk r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]'))
twitter_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="like"]'))
tiktok_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-e2e="follow-button"]'))
#instagram_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class=" _acan _acap _acas _aj1- _ap30"]'))
youtube_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m"]'))
youtube_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start"]'))
facebook_like_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Like"], div[aria-label="Follow"]'))
pintrst_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="user-follow-button"] button'))
sndcld_follow_btn = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Follow"]'))

btns_list = [twitter_follow_btn, twitter_like_btn, tiktok_follow_btn, youtube_follow_btn, youtube_like_btn, pintrst_follow_btn, sndcld_follow_btn, facebook_like_btn, facebook_like_btn, facebook_like_btn]
urls_list = ['/earn-twitter.php', '/earn-twitter-favorites.php', '/earn-tiktok-follow.php', '/earn-youtube-subscribe.php','/earn-youtube.php', '/earn-pinterest-follow.php', '/earn-soundcloud-follow.php', '/earn-facebook.php', '/earn-facebook-subscribes.php', '/earn-facebook-user-follow.php']
main_url = 'https://www.like4like.org/user'
driver.get(f"https://www.like4like.org/login/")
i = 0
j = 0
time.sleep(120)
for btn, url in zip(btns_list, urls_list):
    driver.get("https://www.like4like.org/user" + url)
    try:
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(1))
        original_window = driver.current_window_handle
    except Exception as e:
        print('aaa')
        break
    while True:

        try:
            button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id^=likebutton] a')))
            driver.execute_script("arguments[0].click();", button)
        except Exception as e:
            print('task button not found!')
            break

        try:
            WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
        except Exception as e:
            print('second window did not came!', e)
            break

        time.sleep(5)

        try:
            follow_btn = WebDriverWait(driver, 60).until(btn)
            driver.execute_script("arguments[0].click();", follow_btn)
            time.sleep(2)
            driver.close()
        except Exception as e:
            print('follow/like button not found!')
            driver.close()
            continue

        time.sleep(3)

        try:
            driver.switch_to.window(original_window)
            confirm_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'pulse-checkBox')))
            driver.execute_script("arguments[0].click();", confirm_button)
            time.sleep(5)
        except Exception as e:
            print('confirm button not found!')
            continue

