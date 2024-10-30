# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    options = AppiumOptions()
    options.load_capabilities(
        {
            'platformName': 'iOS',
            'appium:bundleId': 'com.zeonapps.zeon',
            'appium:automationName': 'XCUITest',
            'appium:udid': '1FCDF13C-83ED-4EDD-A91B-B45D3CB1C84B',
            'appium:xcodeSigningId': 'iPhone Developer',
            'appium:xcodeOrgId': 'B5WCG7SAN3',
            'appium:includeSafariInWebviews': True,
            'appium:newCommandTimeout': 3600,
            'appium:connectHardwareKeyboard': True
        }
    )

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

    # XPath locators
    more_bottom_navbar_xpath = '//XCUIElementTypeImage[@name="More"]'
    login_signup_profile_page_xpath = '//XCUIElementTypeImage[@name="Login or Sign Up"]'
    get_otp_button_login_page_xpath = '//XCUIElementTypeStaticText[@name="Get OTP"]'
    enter_name_signup_page_xpath = (
        '//XCUIElementTypeTextField[@name="Enter your full name"]'
    )
    enter_email_signup_page_xpath = (
        '//XCUIElementTypeTextField[@name="Enter your mail ID"]'
    )
    save_signup_page_xpath = '//XCUIElementTypeStaticText[@name="Save & Proceed"]'
    enter_otp_verify_otp_page_xpath = '//XCUIElementTypeTextField'
    select_manufacturer_dropdown_xpath = (
        '//XCUIElementTypeButton[@name="Select Manufacturer"]'
    )
    manufacturer_abb_dropdown_xpath = '//XCUIElementTypeStaticText[@name="ABB"]'
    select_model_dropdown_xpath = '//XCUIElementTypeButton[@name="Select Model"]'
    model_ee_dropdown_xpath = '//XCUIElementTypeStaticText[@name="ee"]'
    temp_number_checkbox_xpath = '//XCUIElementTypeSwitch[@value="0"]'
    temp_number_input_xpath = '//XCUIElementTypeTextField[@name="Enter vehicle number"]'
    save_vehicle_button_xpath = '//XCUIElementTypeStaticText[@name="Save Vehicle"]'

    # Accessibility IDs
    more_button_accessibility_id = 'More'
    login_signup_button_accessibility_id = 'Login or Sign Up'
    get_otp_button_accessibility_id = 'Get OTP'
    enter_full_name_accessibility_id = 'Enter your full name'
    enter_mail_id_accessibility_id = 'Enter your mail ID'
    save_and_proceed_accessibility_id = 'Save & Proceed'
    select_manufacturer_accessibility_id = 'Select Manufacturer'
    abb_manufacturer_accessibility_id = 'ABB'
    select_model_accessibility_id = 'Select Model'
    ee_model_accessibility_id = 'ee'
    enter_vehicle_number_accessibility_id = 'Enter vehicle number'
    save_vehicle_accessibility_id = 'Save Vehicle'

    # Class names
    phone_number_input_class_name = 'XCUIElementTypeTextField'
    temp_number_switch_class_name = 'XCUIElementTypeSwitch'

    # app opened in dashboard
    try:
        # more bottom navbar click
        el1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, more_button_accessibility_id)
            )
        )
        el1.click()
        print("Clicked on 'More' button")

        # Wait for "Login or Sign Up" button and click
        el2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, login_signup_button_accessibility_id)
            )
        )
        el2.click()
        print("Clicked on 'Login or Sign Up'")

        # Wait for the phone number input field and enter the number
        el3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.CLASS_NAME, phone_number_input_class_name)
            )
        )
        el3.send_keys('9876988762')
        print('Phone number entered successfully')

        # Wait for the "Get OTP" button and click
        el4 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, get_otp_button_accessibility_id)
            )
        )
        el4.click()
        print("Clicked on 'Get OTP' button")

        time.sleep(2)

        # Wait for OTP input field and enter the OTP
        el5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, enter_otp_verify_otp_page_xpath)
            )
        )
        el5.send_keys('0101')
        print('OTP entered successfully')
        
        time.sleep(2)

        # Wait for "Enter your full name" field and enter name
        el6 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, enter_full_name_accessibility_id)
            )
        )
        el6.send_keys('Enter Name here')
        print('Name entered successfully')

        # Wait for "Enter your mail ID" field and enter email
        el7 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, enter_mail_id_accessibility_id)
            )
        )
        el7.send_keys('new1@gmail.com')
        driver.hide_keyboard()
        print('Email entered successfully')

        # Wait for "Save & Proceed" button and click
        el8 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, save_and_proceed_accessibility_id)
            )
        )
        el8.click()
    
        print("Clicked on 'Save & Proceed'")
        time.sleep(2)

        # Wait for "Select Manufacturer" dropdown and click
        el9 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, select_manufacturer_accessibility_id)
            )
        )
        el9.click()
        print("Clicked on 'Select Manufacturer'")

        # Wait for "ABB" option and click
        el10 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, abb_manufacturer_accessibility_id)
            )
        )
        el10.click()
        print("Selected 'ABB' as Manufacturer")

        # Wait for "Select Model" dropdown and click
        el11 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, select_model_accessibility_id)
            )
        )
        el11.click()
        print("Clicked on 'Select Model'")

        # Wait for "ee" model option and click
        el12 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, ee_model_accessibility_id)
            )
        )
        el12.click()
        print("Selected 'ee' model")

        # Wait for the temporary number switch and toggle
        el13 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.CLASS_NAME, temp_number_switch_class_name)
            )
        )
        el13.click()
        print('Temporary number switch toggled')

        # Wait for "Enter vehicle number" field and enter vehicle number
        el14 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, enter_vehicle_number_accessibility_id)
            )
        )
        el14.send_keys('vehicleno')
        print('Vehicle number entered successfully')

        # Wait for "Save Vehicle" button and click
        el15 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, save_vehicle_accessibility_id)
            )
        )
        el15.click()
        print("Clicked on 'Save Vehicle'")
        time.sleep(2)
    except Exception as e:
        print(e)
    # driver.quit()
except Exception as e:
    print(e)
