from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://alnafi.com")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn-light') and contains(text(), 'Login')]"))
    )

    login_button.click()

    print("Clicked on the Login button.")
    time.sleep(2)
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    email_field.send_keys("Email")
    password_field.send_keys("Password")

    print("Filled in the email and password fields.")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    login_button.click()

    print("Clicked on the Login button.")
    
    time.sleep(5)
    driver.get("URL_FOR_SPECIFIC_COURSE")

    print("Navigated to the desired URL.")
    try:
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))

        buttons = driver.find_elements(By.TAG_NAME, "button")

        time.sleep(3)

        add_to_cart_button = None
        for button in buttons:
            if "Add to cart" in button.text:
                add_to_cart_button = button
                break

        if add_to_cart_button:
            print("Found the 'Add to cart' button.")
            add_to_cart_button.click()
            print("Clicked on the 'Add to cart' button.")
        else:
            print("Failed to find the 'Add to cart' button.")
    except Exception as e:
        print("An error occurred:", e)

    popup_image = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@src='/Courses/cancel.png']"))
    )

    popup_image.click()

    print("Closed the popup.")
    
    time.sleep(3)

    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Go to Checkout')]"))
    )

    checkout_button.click()

    print("Clicked on the Go to Checkout button.")
    
    time.sleep(3)
    try:
        e_pay_span = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'text-rangoonGreen') and contains(text(), 'Annaafi E-Pay')]"))
        )
        
        driver.execute_script("arguments[0].scrollIntoView(true);", e_pay_span)
        
        e_pay_span.click()
        
        print("Clicked on 'Annaafi E-Pay'.")
    except Exception as e:
        print("An error occurred while clicking on 'Annaafi E-Pay':", e)
    time.sleep(2)
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Checkout')]"))
    )
    
    checkout_button.click()
    
    print("Clicked on the Checkout button.")
    try:
        popup_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='swal2-html-container' and text()='Epay Bill has sent to your email']"))
        )

        print("Pop-up with the message 'Epay Bill has sent to your email' is displayed.")
    except e:
        print("Pop-up with the message 'Epay Bill has sent to your email' is not displayed.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    input("Press Enter to quit...")
    driver.quit()
