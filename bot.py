from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pickle

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://claim.poopzter.app/")

# Load cookies
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh untuk aktifkan session
driver.get("https://claim.poopzter.app/")

while True:
    try:
        time.sleep(5)
        claim_btn = driver.find_element(By.XPATH, '//button[contains(text(), "Claim")]')
        claim_btn.click()
        print("Klaim berhasil!")
    except Exception as e:
        print("Gagal klaim:", str(e))

    print("Tunggu 60 detik...")
    time.sleep(60)
