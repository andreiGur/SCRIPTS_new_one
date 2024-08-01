from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def telegram_alert(message):
    telegaAPIurl1 = "https://api.telegram.org/bot5520811460:AAEiMSM8ZozY6EHVEEeTGeX3oyGxdzHRVC0/sendMessage?chat_id=@CloackerNotify&text=%7B"
    telegaAPIurl2 = "%7D"
    driver = buid_driver_fun()
    driver.get(telegaAPIurl1 + message + telegaAPIurl2)
    driver.close()

def buid_driver_fun():
    driver_path = "C:\\seleniumStuff\\Lamda_python_selenium\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    return driver

def main():
    production_domains = [
        "https://www.wehavethebestgames.info/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5&id_app=hyxtuthjeiged&gl_app=uttrbxmfpdtvexw&admob_app=mdegcdkipwojrqjaxcc",
        "https://www.registrationneedclick.com/apps-maker.php?website=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5",
        "https://www.funwebsitegames.info/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5",
        "https://www.smartappsmobi.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5",
        "https://globalservicesfree.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5"
    ]

    clocking_Url = [
        "https://presstoplayfun.com/index.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u",
        "https://presstoplayfun.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u",
        "https://presstoplayfun.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=",
        "https://stopeatvegan.com/index.php?dapn=5452-test-regular-amazon",
        "https://stopeatvegan.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u",
        "https://stopeatvegan.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=",
        "https://globalwarmingindicator.com/index.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u",
        "https://globalwarmingindicator.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u",
        "https://globalwarmingindicator.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4="
    ]

    responseArr = [""] * len(clocking_Url)

    driver = buid_driver_fun()

    for domain in production_domains:
        driver.get(domain)
        telegram_alert(domain)
        time.sleep(3)

    for i, url in enumerate(clocking_Url):
        driver.get(url)
        telegram_alert(url)
        time.sleep(3)
        responseArr[i] = driver.find_element(By.XPATH, "/html/body").text

    for response in responseArr:
        driver.get(response)
        telegram_alert(response)
        time.sleep(6)
        print(response)

    driver.close()

    driver_system = buid_driver_fun()
    driver_system.get("http://mobileservicesnow.in")
    driver_system.maximize_window()
    driver_system.find_element(By.XPATH, "//*[@id='login']").send_keys("andrei")
    driver_system.find_element(By.XPATH, "//*[@id='pass']").send_keys("jvQ*U0y0)Flh0n3H")
    driver_system.find_element(By.XPATH, "//*[@id='main']/div[1]/form/input[3]").click()
    driver_system.get("http://mobileservicesnow.in/checking/last-100-search-today.php")
    driver_system.find_element(By.XPATH, "/html/body/form/input[8]").send_keys("5452")
    driver_system.find_element(By.XPATH, "/html/body/form/input[10]").click()

if __name__ == "__main__":
    main()
