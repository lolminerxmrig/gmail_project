import random
import time
import pyperclip
import requests
from browser import Driver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


class SMSHub:
    proxies = {
        'http': 'socks5://trojvn:dfv67tg@45.132.106.122:1080',
        'https': 'socks5://trojvn:dfv67tg@45.132.106.122:1080'
    }
    url = "https://smshub.org/stubs/handler_api.php"
    smshub_api = "18440U8268da00bd98efd06eae90438fd07699"
    current_number = None
    current_id = None
    code = None

    @staticmethod
    def get_numbers_status():
        payload = {"api_key": SMSHub.smshub_api,
                   "action": "getNumbersStatus",
                   "country": 0,
                   "operator": "beeline"}
        r = requests.post(SMSHub.url, params=payload, proxies=SMSHub.proxies)
        result = r.json()
        return result["go_0"]

    @staticmethod
    def get_balance():
        payload = {"api_key": SMSHub.smshub_api,
                   "action": "getBalance"}
        r = requests.post(SMSHub.url, params=payload, proxies=SMSHub.proxies)
        result = r.text
        balance = float(result.replace("ACCESS_BALANCE:", ""))
        return balance

    @staticmethod
    def get_number():
        payload = {"api_key": SMSHub.smshub_api,
                   "action": "getNumber",
                   "service": "go",
                   "operator": "any",
                   "country": 0}
        r = requests.post(SMSHub.url, params=payload, proxies=SMSHub.proxies)
        result = r.text
        if "ACCESS_NUMBER" in result:
            result = result.split(":")
            SMSHub.current_id = result[1]
            SMSHub.current_number = result[2]
            return True
        else:
            return False

    @staticmethod
    def set_retry_status():
        payload = {"api_key": SMSHub.smshub_api,
                   "action": "setStatus",
                   "status": "3",
                   "id": SMSHub.current_id}
        r = requests.post(SMSHub.url, params=payload, proxies=SMSHub.proxies)
        result = r.text
        return result

    @staticmethod
    def set_cancel_status():
        payload = {"api_key": SMSHub.smshub_api,
                   "action": "setStatus",
                   "status": "8",
                   "id": SMSHub.current_id}
        r = requests.post(SMSHub.url, params=payload, proxies=SMSHub.proxies)
        result = r.text
        return result

    @staticmethod
    def get_status():
        payload = {"api_key": SMSHub.smshub_api,
                   "action": "getStatus",
                   "id": SMSHub.current_id}
        r = requests.post(SMSHub.url, params=payload, proxies=SMSHub.proxies)
        result = r.text
        if "STATUS_WAIT_CODE" not in result:
            SMSHub.code = result.split(":")[1]
            return True
        else:
            return False


def main():
    d = Driver("selenium")
    d.get("https://google.com/")
    time.sleep(1)

    firstname = "Мамед"
    lastname = "Юхранов"
    username = "mrx.mamed17"
    password = "DFc45#EDF"

    move = d.driver.find_element_by_xpath("//*[text()='Войти']")
    click = ActionChains(d.driver).move_to_element(move).perform()
    time.sleep(1)
    ActionChains(d.driver).click(click).perform()

    move = d.driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
    click = ActionChains(d.driver).move_to_element(move).perform()
    time.sleep(1)
    ActionChains(d.driver).click(click).perform()

    move = d.driver.find_element_by_xpath("//*[text()='Для себя']")
    click = ActionChains(d.driver).move_to_element(move).perform()
    time.sleep(1)
    ActionChains(d.driver).click(click).perform()
    time.sleep(random.randint(3, 5))

    pyperclip.copy(firstname)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyperclip.copy(lastname)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(username, interval=0.1)
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(password, interval=0.1)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(password, interval=0.1)
    pyautogui.press("enter")
    time.sleep(random.randint(7, 14))

    if d.v_check("//*[contains(text(),'SMS')]", timeout=30):
        print("Check 1 success!")
        for i in range(5):
            if SMSHub.get_number():
                break
            time.sleep(1)
        if SMSHub.current_id is None:
            d.stop("Номер не получен. Выход...")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.typewrite(SMSHub.current_number[1:], interval=0.1)  # current_number[1:] без 7
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(random.randint(7, 14))
        for i in range(5):
            print(f"[{i}] попытка получения кода смс...")
            if SMSHub.get_status():
                pyautogui.typewrite(SMSHub.code, interval=0.1)
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(random.randint(7, 14))
            time.sleep(10)
        if SMSHub.code is None:
            print("Код так и не пришел...")
            SMSHub.set_cancel_status()
            d.stop("Выход...")
        else:
            d.v_clear("//input[@id='phoneNumberId']")
            time.sleep(1)
            day = str(random.randint(1, 27))
            d.v_sendkeys("//input[@id='day']", day)
            time.sleep(1)
            month = random.randint(1, 12)
            d.p_click(f"//select[@id='month']/option[@value='{month}']")
            time.sleep(1)
            year = str(random.randint(1980, 1999))
            d.v_sendkeys("//input[@id='year']", year)
            time.sleep(1)
            gender = str(random.randint(1, 2))
            d.p_click(f"//select[@id='gender']/option[@value='{gender}']")
            time.sleep(1)
            d.v_click("//*[text()='Далее']")
            time.sleep(1)
            d.v_click("//*[text()='Принимаю']")
    else:
        print("Check 1 fail!")

    time.sleep(15)
    d.stop("Работа завершена!")
