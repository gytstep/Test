from selenium import webdriver 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://demo.betgames.tv/")
driver.maximize_window()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "betgames_iframe")))
driver.switch_to.frame("betgames_iframe")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "place-bet-button")))
WebDriverWait(driver, 60).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME, "aWwasUYEOnh7FtcLtFMQ.p0jkWKhDz26_IqZHLxCQ")))

bet_button = driver.find_element(By.CLASS_NAME, "iRGX2h7OO48Hztwp3xPI.uj1x8tWyqNFQHF50nb4M")
bet_button.click()

time.sleep(0.5)

amount_button = driver.find_elements(By.CLASS_NAME, "Jn_N1pZAR76SxfnblhBk")
amount_button[2].click()

time.sleep(0.5)

amount_button[3].click()

time.sleep(0.5)

place_bet = driver.find_element(By.CLASS_NAME, "place-bet-button")
place_bet.click()


 