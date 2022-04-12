from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\\Users\\Hp EliteBook\\Desktop\\chrome Driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email= driver.find_element_by_name("email")
f_name.send_keys("Ibukun")
l_name.send_keys("Babatunde")
email.send_keys("stdave001@gmail.com")
button =driver.find_element_by_xpath("/html/body/form/button")
button.click()