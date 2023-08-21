import json
import logging
import os.path
import random
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from static import PROJECT_ROOT_PATH
from .scroll_wait_time import ScrollWaitTime
from .utils import randmized_sleep
from .header_list import FAKE_HEADERS

CHROMEDRIVER_FILE_PATH = f"{PROJECT_ROOT_PATH}/bins/chromedriver"
ADBLOCK_CRX_FILE_PATH = f"{PROJECT_ROOT_PATH}/bins/adblock.crx"


def get_header():
    return FAKE_HEADERS[random.randint(0, len(FAKE_HEADERS))]['User-Agent']


class Browser:
    def __init__(self, has_screen):
        try:
            # Network Performance
            # self.ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

            caps = DesiredCapabilities.CHROME
            caps['goog:loggingPrefs'] = {'performance': 'ALL'}

            # dir_path = os.path.dirname(os.path.realpath(__file__))
            service_args = [f"--ignore-ssl-errors=true, --verbose"]
            chrome_options = Options()
            if not has_screen:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--window-size=1920x1080")
                # chrome_options.set_headless(True)
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--no-sandbox")
            # chrome_options.add_extension(ADBLOCK_CRX_FILE_PATH)
            # chrome_options.add_argument(f"user-agent={ua['google chrome']}")
            # chrome_options.add_argument(f"user-agent={get_header()}")
            # "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
            chrome_options.add_argument(
                "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            )
            # chrome_options.add_argument(f"lang=ko_KR")

            self.driver = webdriver.Chrome(
                # executable_path=f"{dir_path}/bin/chromedriver",
                executable_path=CHROMEDRIVER_FILE_PATH,
                service_args=service_args,
                chrome_options=chrome_options,
                desired_capabilities=caps,  # Network Performance
            )
            self.driver.implicitly_wait(3.0)
            self.driver.minimize_window()
        except Exception as e:
            logging.warning(e)

    def page_source(self):
        return self.driver.page_source

    @property
    def page_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def get(self, url):
        self.driver.get(url)

    @property
    def cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name: str):
        return self.driver.get_cookie(name)

    def add_coocie(self, cookie_dict: dict):
        return self.driver.add_cookie(cookie_dict)

    @property
    def current_url(self):
        return self.driver.current_url

    def implicitly_wait(self, t):
        self.driver.implicitly_wait(t)

    def close(self):
        self.driver.close()

    def find_one(self, css_selector, elem=None, waittime=10):
        obj = elem or self.driver
        if waittime:
            WebDriverWait(obj, waittime).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
        try:
            return obj.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None
        except StaleElementReferenceException as e:
            logging.warning(e)
            return None

    def execute_script(self, script, args=None):
        try:
            return self.driver.execute_script(script, args)
        except Exception as e:
            logging.exception(e)
            return None

    def screen_size_70_percent(self):
        self.driver.execute_script("document.body.style.zoom = '0.70'")  # 스크린 배율 뒤로 작게 -- 스크롤이 중간으로 강제 이동 되는 현상이 있음.

    def action_chains(self, keys: Keys):
        action = ActionChains(self.driver)
        action.send_keys(keys)
        action.perform()

    def move_to_element_and_click(self, el):
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        action.move_to_element(el).click().perform()

    def find(self, css_selector, elem=None, waittime=2):
        obj = elem or self.driver
        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
                )
        except TimeoutException as e:
            logging.warning(css_selector)
            return None
        except StaleElementReferenceException as e:
            logging.warning(e)
            return None

        try:
            return obj.find_elements(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None
        except StaleElementReferenceException as e:
            logging.warning(e)
            return None

    def find_xpath(self, xpath, elem=None, waittime=0):
        obj = elem or self.driver

        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
        except TimeoutException as e:
            logging.warning(f"Timeout, xpath: {xpath}, elem: {elem}")
            return None
        except StaleElementReferenceException as e:
            logging.warning(e)
            return None

        try:
            return obj.find_elements(By.XPATH, xpath)
        except NoSuchElementException as e:
            logging.warning(xpath)
            return None
        except StaleElementReferenceException as e:
            logging.warning(e)
            return None

    def scroll_down(self, offset=0, wait=1):
        if ScrollWaitTime.wait_time is not None:
            wait = ScrollWaitTime.wait_time
        if offset == 0:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        else:
            self.driver.execute_script("window.scrollBy(0, %s)" % offset)
        randmized_sleep(wait)

    def scroll_up(self, offset=-1, wait=2):
        if offset == -1:
            self.driver.execute_script("window.scrollTo(0, 0)")
        else:
            self.driver.execute_script("window.scrollBy(0, -%s)" % offset)
        randmized_sleep(wait)

    def js_click(self, elem):
        self.driver.execute_script("arguments[0].click();", elem)

    def open_new_tab(self, url):
        self.driver.execute_script("window.open('%s');" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_current_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def __del__(self):
        try:
            self.driver.quit()
        except Exception as e:
            logging.warning("Driver Quited")
            pass

    @staticmethod
    def __process_browser_log_entry(entry):
        response = json.loads(entry['message'])['message']
        return response

    def get_browser_log(self):
        browser_log = self.driver.get_log('performance')
        events = [self.__process_browser_log_entry(entry) for entry in browser_log]
        events = [event["params"] for event in events if 'Network.response' in event['method']]
        events = [event["response"] for event in events if "response" in event]
        events = [event for event in events if "headers" in event]
        ret = []
        for event in events:
            if "headers" in event:
                _depth1 = event["headers"]
                if "content-type" in _depth1:
                    _depth2 = _depth1["content-type"]
                    if _depth2 == "video/mp4":
                        ret.append(event)
        return ret

    def get_raw_browser_log(self):
        browser_log = self.driver.get_log('performance')
        events = [self.__process_browser_log_entry(entry) for entry in browser_log]
        return str(events)
