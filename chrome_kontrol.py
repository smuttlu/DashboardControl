import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--start-maximized")


options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-proxy-server")  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def open_page():
    driver.get( 				url adresini giriniz)
    time.sleep(2)

def paste_text(text):
    pyautogui.write(text, interval=0.05)

def press_key(key):
    pyautogui.press(key)

def login():
    print("Oturum kapanmış! Yeniden giriş yapılıyor...")

    paste_text( 				kullanıcı adı bilgisi)
    press_key("tab")
    time.sleep(0.5)
    paste_text(					sifre bilgisi)
    press_key("enter")

    print("Yeniden giriş yapıldı!")

open_page()
login()

while True:
    time.sleep(60)
    try:
        
        if not driver.current_url.startswith( 			sayfanın kapanıp kapanmadığını kontrol etmek icin tekrar url giriniz):
            print("Sayfa kapanmış, tekrar açılıyor...")
            open_page()
            login()
        else:
            driver.refresh()
    except:
        print("Tarayıcı kapanmış, yeniden başlatılıyor...")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        open_page()
        login()
