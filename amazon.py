from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Define desired capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "app": "C:\\Users\\Win-11\\PycharmProjects\\pythonPrime\\Amazon_28.13.0.300.apk",
    "automationName": "UiAutomator2"
}


capabilities_option = UiAutomator2Options().load_capabilities(desired_caps)
print("im in cap")

    # Connect to Appium server
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_option)
print("driver")


driver.quit()
