from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = akinyeleshakirullahi2018@gmail.com
ACCOUNT_PASSWORD = Akinshak215429
PHONE = 8148269678

chrome_driver_path = "C:\Users\PYTHAGON\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# GETTING THE LINK AND RUNNING IT
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
 
 time.sleep(5)
# TO CLICK ON THE SIGN IN BUTTON
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

# WAIT FOR THE PAGE TO LOAD
time.sleep(7)

# INFORMATION TO LOGIN 
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)

password.send_keys(Keys.ENTER)

# LOCATE THE APPLY BUTTON 
time.sleep(7)
all_listings = driver.find_element_by_css_selector(".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # LOCATE THE APPLY BUTTON IF NOT,SKIP THE JOB
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        # INPUT YOUR NUMBER IF FIELD EMPTY

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")
# TEST FOR MULTI STEP APPLICATION
# IF THE submit_button IS A 'Next' button,then this is a multi step APPLICATION
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(3)

            discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            time.sleep(2)
            print("Complex Application, Skipped.")
            continue 
        else:
            submit_button.click()
        # Close Window once Application Completed
        time.sleep(5)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied or Job no longer accepting APPLICATION,Then Skip
    except NoSuchElementException:
        print("No Application Button, Skipped.")
        continue

# END OF APPLICATION
time.sleep(7)
driver.close()