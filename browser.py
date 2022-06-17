import base64
import os
import time
from glob import glob
import asyncio
from threading import Thread
import pproxy
import socket
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth


class Selenoid:
    SELENOID_HOST = "http://127.0.0.1:4444"
    SELENOID_DOWNLOAD_URL = f"{SELENOID_HOST}/download/"
    SELENOID_WD_HUB_URL = f"{SELENOID_HOST}/wd/hub"

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"

    @staticmethod
    def chrome():
        # Находим все расширения в папке extensions
        crx_list = glob(f"{os.getcwd()}/extensions/*.crx")
        # Записываем в список base64 каждого расширения
        crx_names = []
        for crx in crx_list:
            crx_names.append(base64.b64encode(open(file=crx, mode="rb").read()).decode('UTF-8'))

        # А здесь мы уже работаем с настройками хрома. crx_names это уже список base64 расширений
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "101.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
            },
            "goog:chromeOptions": {
                "args": [f"user-agent={Selenoid.USER_AGENT}", "disable-infobars", "start-maximized",
                         f"proxy-server={BackgroundProxy.LOCAL_HOST}:{BackgroundProxy.LOCAL_PORT}",
                         "disable-blink-features=AutomationControlled", "no-sandbox"],
                "excludeSwitches": ["enable-automation"],
                "useAutomationExtension": False,
                "extensions": crx_names,
                "prefs": {
                    "profile.default_content_setting_values.media_stream_mic": 2,
                    "profile.default_content_setting_values.media_stream_camera": 2,
                    "profile.default_content_setting_values.geolocation": 2,
                    "profile.default_content_setting_values.notifications": 2
                }
            }
        }

        # Возвращаем DRIVER
        return webdriver.Remote(
            command_executor=Selenoid.SELENOID_WD_HUB_URL,
            desired_capabilities=capabilities)


class Selenium:
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
    # USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1"
    # USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1"

    @staticmethod
    def chrome():
        options = webdriver.ChromeOptions()
        prefs = {
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2,
            "download.default_directory": f"{os.getcwd()}/data"
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("disable-notifications")
        options.add_argument("disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("disable-blink-features=AutomationControlled")
        # options.add_argument("user-data-dir=/home/trojvn/.config/chromium/")
        # options.add_argument("profile-directory=Default")
        # options.add_argument("profile-directory=Profile2")
        # options.add_argument(f"proxy-server={BackgroundProxy.LOCAL_HOST}:{BackgroundProxy.LOCAL_PORT}")
        crx_list = glob("./extensions/*.crx")
        for crx in crx_list:
            options.add_extension(crx)
        driver = webdriver.Chrome(executable_path="chromedriver", options=options)
        # stealth(driver,
        #         user_agent=Selenium.USER_AGENT,
        #         # languages=["ru-RU", "ru"],
        #         languages=["en-US", "en"],
        #         # languages=["uk-UA", "uk"],
        #         # vendor="Apple Computer, Inc.",
        #         # platform="Win32",
        #         # webgl_vendor="Apple Inc.",
        #         # renderer="Apple GPU",
        #         fix_hairline=True,
        #         )
        # driver.implicitly_wait(90)
        # driver.set_page_load_timeout(90)
        return driver


class Driver:
    __slots__ = "driver"

    def __init__(self, type_):
        BackgroundProxy.start()
        if type_ == "selenium":
            self.driver = Selenium.chrome()
        else:
            self.driver = Selenoid.chrome()

    def get(self, url):
        try:
            self.driver.get(url)
        except Exception as E:
            self.stop(E)

    def v_check(self, xpath, timeout=10):
        try:
            return WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except Exception as E:
            print(E)
            return False

    def v_check_array(self, xpath, timeout=10):
        try:
            return WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        except Exception as E:
            print(E)
            return False

    def v_click(self, xpath, timeout=10):
        try:
            WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))).click()
        except Exception as E:
            self.stop(E)

    def v_clear(self, xpath, timeout=10):
        try:
            WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))).clear()
        except Exception as E:
            self.stop(E)

    def v_sendkeys(self, xpath, text, timeout=10):
        try:
            WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(text)
        except Exception as E:
            self.stop(E)

    def p_check(self, xpath, timeout=10):
        try:
            return WebDriverWait(
                self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except Exception as E:
            print(E)
            return False

    def p_check_array(self, xpath, timeout=10):
        try:
            return WebDriverWait(
                self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath)))
        except Exception as E:
            print(E)
            return False

    def p_click(self, xpath, timeout=10):
        try:
            WebDriverWait(
                self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))).click()
        except Exception as E:
            self.stop(E)

    def p_clear(self, xpath, timeout=10):
        try:
            WebDriverWait(
                self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))).clear()
        except Exception as E:
            self.stop(E)

    def p_sendkeys(self, xpath, text, timeout=10):
        try:
            WebDriverWait(
                self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))).send_keys(text)
        except Exception as E:
            self.stop(E)

    def stop(self, E):
        print(E)
        self.driver.quit()
        BackgroundProxy.stop()
        raise SystemExit

    def download_cookies_from_container(self, cookies_new_name_path):
        response = requests.get(f"{Selenoid.SELENOID_DOWNLOAD_URL}{self.driver.session_id}/cookiebro-cookies.json")
        if not response.status_code == 404:
            with open(cookies_new_name_path, "wb+") as f:
                f.write(response.content)
            return True
        elif response.status_code == 404:
            return False

    def export_cookies_from_container(self, cookies_new_name):
        try:
            self.driver.get("chrome-extension://lpmockibcakojclnfmhchibmdpmollgn/editor.html")
            self.v_click("/html/body/div[1]/div/div[1]/div[1]/img[5]")
            for _ in range(10):
                if self.download_cookies_from_container(cookies_new_name):
                    break
        except Exception as E:
            self.stop(E)

    def export_cookies_from_selenium(self, cookies_new_name_path):
        cookiebro_path = f"{os.getcwd()}/data/cookiebro-cookies.json"
        try:
            os.remove(cookiebro_path)
        except Exception as E:
            print(E)
        self.driver.get("chrome-extension://lpmockibcakojclnfmhchibmdpmollgn/editor.html")
        time.sleep(1)
        self.v_click("/html/body/div[1]/div/div[1]/div[1]/img[5]")
        time.sleep(7)
        try:
            os.remove(cookies_new_name_path)
        except Exception as E:
            print(E)
        os.rename(cookiebro_path, cookies_new_name_path)

    def import_cookies_from_container(self, cookies_json_file_path):
        self.driver.get("chrome-extension://lpmockibcakojclnfmhchibmdpmollgn/editor.html")
        send_json = self.p_check("//input[@type='file']")
        try:
            self.driver.file_detector = LocalFileDetector()
            send_json.send_keys(cookies_json_file_path)
        except Exception as E:
            self.stop(E)

    def import_cookies_from_selenium(self, cookies_json_file_path):
        self.driver.get("chrome-extension://lpmockibcakojclnfmhchibmdpmollgn/editor.html")
        self.p_sendkeys("//input[@type='file']", f"{os.getcwd()}/{cookies_json_file_path}")


class BackgroundProxy:
    LOOP_PROXY = asyncio.get_event_loop()
    LOCAL_HOST = "127.0.0.1"
    LOCAL_PORT = 10000

    @staticmethod
    def __check_port(localPort):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((BackgroundProxy.LOCAL_HOST, localPort))
            s.close()
            return True
        except socket.error:
            return False

    @staticmethod
    def __get_free_port():
        while not BackgroundProxy.__check_port(localPort=BackgroundProxy.LOCAL_PORT):
            BackgroundProxy.LOCAL_PORT += 1
        return True

    @staticmethod
    def __start_pproxy(ip, auth, localPort):
        server = pproxy.Server(f'http://{BackgroundProxy.LOCAL_HOST}:{localPort}')
        remote = pproxy.Connection(f'http+socks4+socks5://{ip}#{auth}')
        args = dict(rserver=[remote], verbose=print)
        BackgroundProxy.LOOP_PROXY.run_until_complete(server.start_server(args))

    @staticmethod
    def __start():
        def __start_forever(loop):
            loop.run_forever()

        thread = Thread(target=__start_forever, args=(BackgroundProxy.LOOP_PROXY,))
        thread.start()

    @staticmethod
    def __stop():
        BackgroundProxy.LOOP_PROXY.call_soon_threadsafe(BackgroundProxy.LOOP_PROXY.stop)

    @staticmethod
    def start():
        if BackgroundProxy.__get_free_port():
            ProxyData.main()
            BackgroundProxy.__start_pproxy(ProxyData.PROXY_IP, ProxyData.PROXY_AUTH, BackgroundProxy.LOCAL_PORT)
            BackgroundProxy.__start()

    @staticmethod
    def stop():
        BackgroundProxy.__stop()


class ProxyData:
    PROXY_DICT = []
    PROXY = None
    PROXY_IP = None
    PROXY_AUTH = None
    PROXY_FILE = f"{os.getcwd()}/data/file_proxy.txt"

    @staticmethod
    def __get():
        with open(ProxyData.PROXY_FILE, "r") as f:
            ProxyData.PROXY_DICT = f.readlines()
        if ProxyData.PROXY_DICT:
            ProxyData.PROXY = ProxyData.PROXY_DICT[0].rstrip()
            splitter = ";"
            if splitter in ProxyData.PROXY:
                ProxyData.PROXY_IP = ProxyData.PROXY.split(splitter)[0]
                ProxyData.PROXY_AUTH = ProxyData.PROXY.split(splitter)[1]
            else:
                ProxyData.PROXY_IP = f"{ProxyData.PROXY.split(':')[0]}:{ProxyData.PROXY.split(':')[1]}"
                ProxyData.PROXY_AUTH = f"{ProxyData.PROXY.split(':')[2]}:{ProxyData.PROXY.split(':')[3]}"
            return True
        else:
            print("Отсутствует прокси-сервер в списке")
            return False

    @staticmethod
    def __del():
        with open(ProxyData.PROXY_FILE, "w") as f:
            del ProxyData.PROXY_DICT[0]
            f.writelines(ProxyData.PROXY_DICT)

    @staticmethod
    def __move():
        if "\n" not in ProxyData.PROXY_DICT[-1]:
            ProxyData.PROXY_DICT[-1] += "\n"
        ProxyData.PROXY_DICT.append(f"{ProxyData.PROXY}\n")
        with open(ProxyData.PROXY_FILE, "w") as f:
            f.writelines(ProxyData.PROXY_DICT)

    @staticmethod
    def main():
        if ProxyData.__get():
            ProxyData.__del()
            ProxyData.__move()
