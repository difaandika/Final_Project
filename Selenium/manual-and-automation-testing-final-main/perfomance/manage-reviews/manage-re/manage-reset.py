import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Testlogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs website
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(2)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,"oxd-button").click() #klik button login
        time.sleep(8)
        driver.find_element(By.LINK_TEXT, 'Performance').click() #klik sub performance
        time.sleep(8)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() #klik manage review
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click() #klik manage review pada menu dropdown
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div/div[2]/div/div/input").send_keys("Anthony Nolan") #isi anthony nolan
        time.sleep(4)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div/div[2]/div/div[2]").click() #klik anthony nolan
        time.sleep(4)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() #klik button reset
        time.sleep(7)
        
        
        #validasi
        response_message = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div/div[1]/label").text
        self.assertEqual(response_message, 'Employee Name')

    
unittest.main()