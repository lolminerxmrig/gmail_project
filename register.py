import random
import time
import pyperclip
from browser import Driver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


def main(locker):
    locker.acquire()
    d = Driver("selenium")
    d.get("https://google.com/")
    time.sleep(1)

    firstname = "Мамед"
    lastname = "Юхранов"
    username = "mrx.mamed17"
    password = "DFc45#EDF"

    locker.release()

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

    # pyautogui.hotkey("alt", "shift")
    # time.sleep(1)
    pyperclip.copy(firstname)
    pyautogui.hotkey("ctrl", "v")
    # pyautogui.typewrite(pyperclip.paste(), interval=0.2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyperclip.copy(lastname)
    pyautogui.hotkey("ctrl", "v")
    # pyautogui.typewrite(pyperclip.paste(), interval=0.2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    # pyautogui.hotkey("alt", "shift")
    # time.sleep(1)
    pyautogui.typewrite(username, interval=0.2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(password, interval=0.2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(password, interval=0.2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    number = "9034276767"
    pyautogui.typewrite(number, interval=0.2)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(random.randint(3, 5))
    code = ""
    pyautogui.typewrite(code, interval=0.2)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(random.randint(3, 5))

    time.sleep(30)
    d.stop("Работа завершена!")


# d.v_clear("//input[@id='phoneNumberId']")
# time.sleep(1)
# day = str(random.randint(1, 27))
# d.v_sendkeys("//input[@id='day']", day)
# time.sleep(1)
# month = random.randint(1, 12)
# d.p_click(f"//select[@id='month']/option[@value='{month}']")
# time.sleep(1)
# year = str(random.randint(1980, 1999))
# d.v_sendkeys("//input[@id='year']", year)
# time.sleep(1)
# gender = str(random.randint(1, 2))
# d.p_click(f"//select[@id='gender']/option[@value='{gender}']")
# time.sleep(1)
# d.v_click("//*[text()='Далее']")
# time.sleep(1)
# d.v_click("//*[text()='Принимаю']")

# time.sleep(1000)
