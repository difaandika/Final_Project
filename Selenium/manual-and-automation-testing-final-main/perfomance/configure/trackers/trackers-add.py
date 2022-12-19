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
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click() #klik configure
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]/a").click() #klik trackers didalam dropdown menu
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #klik add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input").send_keys("arsha") #isi Kevin Mathews 
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("Kevin Mathews") #isi Kevin Mathews 
        time.sleep(8)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div").click() #klik nama Kevin Mathews 
        time.sleep(8)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[1]/input").send_keys("Odis Adalwin") #isi odis adalwin
        time.sleep(8)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div").click() #klik nama Odis Adalwin
        time.sleep(8)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() #klik button save
        time.sleep(10)

        #validasi
        response_message = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[1]/label").text
        self.assertEqual(response_message, 'Employee Name')

    
unittest.main()