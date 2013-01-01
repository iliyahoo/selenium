import time
from config import *
from lib import *

browser = get_firefox()

def DoTest():
    try:
        # Sign out (in case we were logged in)
        browser.delete_all_cookies()
        browser.get("http://www.shopyourway.com")
        # Click on login tab
        browser.find_element_by_id("sign-in-link").click()
        # wait for page to load
        # http://seleniumhq.org/docs/04_webdriver_advanced.html
        time.sleep(5)
        # Go inside auth frame
        browser.switch_to_frame(browser.find_element_by_name("authentication-iframe"))
        # Fill and submit login form
        browser.find_element_by_id("email").send_keys(SYW_USERNAME)
        browser.find_element_by_id("password").send_keys(SYW_PASSWORD)
        browser.find_element_by_id("btn-sign-in").click()
        time.sleep(5)
#        try:
#           browser.find_element_by_id("email")
            # In case of "Bad login"
#            print "Tools login 1"
#           return False
#       except:
#           pass
        # Go to the product page
        browser.get(SYW_PRODUCT_URL)
        time.sleep(5)
        # Click on  "Personal Size Assistant"
        browser.find_element_by_xpath("//div[@data-app-id=1050]").click()
        # Wait till the popup will open
        time.sleep(10)
        # Switch current window to the opened frame
        frame = browser.find_element_by_xpath("//iframe[@data-app-id=1050]")
        browser.switch_to_frame(frame)
        el = browser.find_element_by_xpath("//ul[@class='available-box']")
        if "WOMEN'S" not in el.text:
            return False

    except:
        print "Tools login 2"
        raise
        return False
    finally:
        browser.close()
    return True

result = DoTest()
print "Tools login 0" if result else "Tools login 3"
