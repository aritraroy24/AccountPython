from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def register(user, email, password):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("coin-pump.cc/ref?partner=aritraroy24")

    user = user
    email = email
    password = password
    
    register = driver.find_element_by_class_name('startmining')
    register.click()
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('Email').send_keys(email)
    driver.find_element_by_id('Password').send_keys(password)
    driver.find_element_by_id('Confirmpassword').send_keys(password)
    driver.find_element_by_class_name('registration-action-btn').click()
    time.sleep(5)
    driver.close()



if __name__ == '__main__':
    start = int(input('Enter the starting range: '))
    end = int(input('Enter the ending range: '))
    for i in range(start, end):
        user = "test"+str(i)
        print(user)
        email = user+"@gmail.com"
        password = user+"@12345"
        register(user, email, password)
