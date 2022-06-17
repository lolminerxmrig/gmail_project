import random
import time
from keyboard import press_and_release
import pyperclip
from selenium.webdriver import Keys

from browser import Driver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


# def paste(text: str):
#     pyperclip.copy(text)
#     press_and_release('ctrl + v')
#
#
# def type_(text: str, interval=0.0):
#     buffer = pyperclip.paste()
#     if not interval:
#         paste(text)
#     else:
#         for char in text:
#             paste(char)
#             time.sleep(interval)
#     pyperclip.copy(buffer)

def send_keys_delayed(driver, str):
    for char in str:
        ActionChains(driver).send_keys(char).perform()
        time.sleep(random.uniform(0.03, 0.2))


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

    # sendkeys actions
    # send_keys_delayed(d.driver, "Мамед")
    # # ActionChains(d.driver).send_keys("Мамед").perform()
    # time.sleep(1)
    # ActionChains(d.driver).send_keys(Keys.TAB).perform()
    # time.sleep(1)
    # send_keys_delayed(d.driver, "Юхранов")
    # # ActionChains(d.driver).send_keys("Юхранов").perform()
    # ActionChains(d.driver).send_keys(Keys.TAB).perform()
    # time.sleep(1)
    # send_keys_delayed(d.driver, "mrx.mamed1212")
    # # ActionChains(d.driver).send_keys("mrx.mamed1212").perform()
    # time.sleep(1)
    # ActionChains(d.driver).send_keys(Keys.TAB).perform()
    # time.sleep(1)
    # ActionChains(d.driver).send_keys(Keys.TAB).perform()
    # time.sleep(1)
    # send_keys_delayed(d.driver, "DFc45#EDD")
    # # ActionChains(d.driver).send_keys("DFc45#EDD").perform()
    # time.sleep(1)
    # ActionChains(d.driver).send_keys(Keys.TAB).perform()
    # time.sleep(1)
    # send_keys_delayed(d.driver, "DFc45#EDD")
    # # ActionChains(d.driver).send_keys("DFc45#EDD").perform()
    # time.sleep(1)
    # ActionChains(d.driver).send_keys(Keys.ENTER).perform()

    # sendkeys pyautogui
    # pyautogui.press("tab")
    # time.sleep(1)
    pyautogui.hotkey("alt", "shift")
    time.sleep(1)
    pyautogui.typewrite('Vfvtl', interval=0.2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite('>[hfyjd', interval=0.2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.hotkey("alt", "shift")
    time.sleep(1)
    pyautogui.typewrite('mrx.mamedd123', interval=0.2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite('DFc45#EDD', interval=0.2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite('DFc45#EDD', interval=0.2)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite('9034276767', interval=0.2)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(random.randint(3, 5))
    code = ""
    pyautogui.typewrite(code, interval=0.2)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(random.randint(3, 5))

    # d.driver.find_element_by_xpath("//input[@name='firstName']")
    # move = d.driver.find_element_by_xpath("//input[@name='firstName']")
    # click = ActionChains(d.driver).move_to_element(move).perform()
    # time.sleep(random.randint(3, 5))
    # ActionChains(d.driver).click(click).perform()
    # ActionChains(d.driver).send_keys_to_element(click, firstname).perform()
    # time.sleep(random.randint(3, 5))
    #
    # move = d.driver.find_element_by_xpath("//input[@name='lastName']")
    # click = ActionChains(d.driver).move_to_element(move).perform()
    # time.sleep(random.randint(3, 5))
    # ActionChains(d.driver).click(click).perform()
    # ActionChains(d.driver).send_keys_to_element(click, lastname).perform()
    # time.sleep(random.randint(3, 5))

    # move = d.driver.find_element_by_xpath("//input[@name='Username']")
    # click = ActionChains(d.driver).move_to_element(move).perform()
    # time.sleep(random.randint(3, 5))
    # ActionChains(d.driver).click(click).perform()
    # ActionChains(d.driver).send_keys_to_element(click, username).perform()
    # time.sleep(random.randint(3, 5))
    #
    # move = d.driver.find_element_by_xpath("//input[@name='Passwd']")
    # click = ActionChains(d.driver).move_to_element(move).perform()
    # time.sleep(random.randint(3, 5))
    # ActionChains(d.driver).click(click).perform()
    # ActionChains(d.driver).send_keys_to_element(click, password).perform()
    # time.sleep(random.randint(3, 5))
    #
    # move = d.driver.find_element_by_xpath("//input[@name='ConfirmPasswd']")
    # click = ActionChains(d.driver).move_to_element(move).perform()
    # time.sleep(random.randint(3, 5))
    # ActionChains(d.driver).click(click).perform()
    # ActionChains(d.driver).send_keys_to_element(click, password).perform()
    # time.sleep(random.randint(3, 5))
    #
    #
    # move = d.driver.find_element_by_xpath("//*[text()='Далее']")
    # click = ActionChains(d.driver).move_to_element(move).perform()
    # time.sleep(1)
    # ActionChains(d.driver).click(click).perform()

    time.sleep(30)
    d.stop("Работа завершена!")

# def main(locker):
# locker.acquire()
# d = Driver("selenium")

# firstname = "Мамед"
# lastname = "Юхранов"
# username = "mrx.mamed17"
# password = "DFc45#EDF"

# time.sleep(3)
# locker.release()
# d.get("https://bot.sannysoft.com")
# time.sleep(3)
# d.get("https://google.com")
# time.sleep(1)
# d.v_click("//*[text()='Войти']")
# time.sleep(1)
# d.v_click("//*[text()='Создать аккаунт']")
# time.sleep(1)
# d.v_click("//*[text()='Для себя']")
# time.sleep(1)
# d.v_sendkeys("//input[@name='firstName']", firstname)
# time.sleep(1)
# d.v_sendkeys("//input[@name='lastName']", lastname)
# time.sleep(1)
# d.v_sendkeys("//input[@name='Username']", username)
# time.sleep(1)
# d.v_sendkeys("//input[@name='Passwd']", password)
# time.sleep(1)
# d.v_sendkeys("//input[@name='ConfirmPasswd']", password)
# time.sleep(1)
# d.v_click("//*[text()='Далее']")

# time.sleep(100)

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
