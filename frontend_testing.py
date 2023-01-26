from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from db_connector import get_random_exist_user_id

"""
Frontend testing using selenium
1. Start a Selenium Webdriver session.
2. Navigate to web interface URL using an existing user id.
3. Check that the user name element is showing (web element exists).
4. Print user name (using locator)
"""


def frontendTesting(user_id):
    try:
        driver = webdriver.Chrome(service=Service("C:/Users/Or/Desktop/OrAntebiProject-master/chromedriver"))
        driver.get("http://127.0.0.1:5001/users/get_user_name/" + str(user_id))
        driver.maximize_window()
        driver.implicitly_wait(20)

        user_name_element = driver.find_element(By.ID, value="user_id").text
        print("Test Selenium: PASS\n"
            "user_name is:", user_name_element, "on locator ID: \"user_id\" and it's equal to:", user_id)

    except:
        print("test failed")

    finally:
        driver.quit()


frontendTesting(get_random_exist_user_id())
