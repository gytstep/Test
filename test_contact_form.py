import pytest
from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_ContactForm():

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://demo.betgames.tv/")

    cu_message = driver.find_element(By.NAME, value="message")
    cu_message.send_keys("It's a Me, Mario!")

    cu_email = driver.find_element(By.NAME, value="email")
    cu_email.send_keys("Mario69@gmail.com")

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)

    send_button = driver.find_element(By.CLASS_NAME, value="send.btn.btn-primary")
    send_button.click()
    time.sleep(4)
    driver.close()

