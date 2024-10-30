from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def handle_skip_button(driver, timeout=5):
    try:
        # Wait for the skip button to be present and clickable
        skip_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Skip'))
        )

        # Click the button if found
        skip_button.click()
        print('Skip button found and clicked successfully')
    except Exception as e:
        print('Skip not cliked')


try:
    options = AppiumOptions()
    options.load_capabilities(
        {
            # Basic capabilities
            'platformName': 'iOS',
            'appium:bundleId': 'com.zeonapps.zeon',
            'appium:automationName': 'XCUITest',
            'appium:udid': '1FCDF13C-83ED-4EDD-A91B-B45D3CB1C84B',
            'appium:xcodeSigningId': 'iPhone Developer',
            'appium:xcodeOrgId': 'B5WCG7SAN3',
            'appium:includeSafariInWebviews': True,
            'appium:newCommandTimeout': 3600,
            'appium:connectHardwareKeyboard': True,
            'autoDismissAlerts': True
        }
    )

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    handle_skip_button(driver)
    
    # Wait and find "More" button
    el1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "More"))
    )
    el1.click()

    # Wait and find "Login or Sign Up" button 
    el2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Login or Sign Up"))
    )
    el2.click()

    # Wait and find phone number text field
    el3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.CLASS_NAME, "XCUIElementTypeTextField"))
    )
    el3.send_keys("8680872639")

    # Wait and find "Get OTP" button
    el4 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Get OTP"))
    )
    el4.click()

    # Wait and find OTP text field
    el5 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.CLASS_NAME, "XCUIElementTypeTextField"))
    )
    el5.send_keys("0101")
except Exception as e:
    print(e)
