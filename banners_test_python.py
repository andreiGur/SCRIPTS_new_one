import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = build_driver()
    system_sign_in(driver)
    time.sleep(2)
    driver.maximize_window()
    
    driver.get("https://mobileservicesnow.in/upload_9000/upload-9000.php")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/select/option[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/div[3]/input[2]").click()
    time.sleep(3)
    
    all_links = driver.find_elements(By.TAG_NAME, "a")
    
    telegram_alert("Banners(links) status-check test = START")
    for link in all_links:
        href = link.get_attribute("href")
        if href:
            print("\nLink:", href)
            status_code = request_status_check(href)
            print("Request status code:", status_code)
            if status_code != 200:
                telegram_alert(f"{link.text} - {href}")
                telegram_alert(str(status_code))
            print("\n")
    telegram_alert("Banners(links) status-check test = END")
    
    driver.close()

def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Optional: run in headless mode
    driver = webdriver.Chrome(options=options)
    return driver

def system_sign_in(driver):
    driver.get("http://mobileservicesnow.in")
    driver.maximize_window()
    driver.get("http://mobileservicesnow.in/odds_link_maker.php")
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys("andrei")
    driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("jvQ*U0y0)Flh0n3H")
    driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/form/input[3]').click()

def request_status_check(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")
        return None

def telegram_alert(message):
    api_url = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
    params = {
        "chat_id": "@CloackerNotify",
        "text": message
    }
    try:
        response = requests.get(api_url, params=params)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error sending telegram alert: {e}")
        return None

if __name__ == "__main__":
    main()

