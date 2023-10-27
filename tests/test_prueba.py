'''
Created on 27 oct. 2023

@author: alj70
'''
import unittest

import selenium

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from pages.sambsung_registro import NavHome as Sambsung_registro

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome() 
        self.action = ActionChains(self.driver)
        
        self.driver.maximize_window() 
        self.driver.implicitly_wait(5)
        self.driver.get("https://shop.samsung.com/ar/")
        
        
    def test_001(self): 
        #Móviles:
        try: 
            movil = self.driver.find_element(By.XPATH,Sambsung_registro.xpath_movil)
            self.action.move_to_element(movil).perform()
            time.sleep(3)
        
            self.driver.find_element(By.XPATH,Sambsung_registro.xpath_movil).click()
       
            #Validar Click en link "Moviles":
            assert self.driver.current_url==Sambsung_registro.url_moviles
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
            
            
    def test_0011(self):
        
        #Validar Titulo:
        self.assertEqual(self.driver.title,'Samsung Shop: descubrí la gama completa | Samsung Argentina')

        
    def test_002(self):
        
        #Logo Sambsung (Home):
        sambsung = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/a")
        sambsung.click()
        if sambsung:
            print("the link goes back to home")
        time.sleep(3)
        
        self.assertEqual(self.driver.title,'Samsung Shop: descubrí la gama completa | Samsung Argentina')
    
        
    def test_003(self):
        #Validar title.isupper()
        self.assertFalse(self.driver.title.isupper())

    def test_004(self):
        #TV & Audio:
        try:          
            tv_audio = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/div/div/div[1]/ul/li[2]")
            self.action.move_to_element(tv_audio).perform()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/div/div/div[1]/ul/li[2]").click()#Click enlace
            
            #Validar Click en link "TV & Audio":
            assert self.driver.current_url=='https://shop.samsung.com/ar/tv-av?order=OrderByReleaseDateDESC'
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/a").click()#Click Home (Sambsung)
            
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        

    def test_005(self):
        #Electrodomesticos:
        try:
            
            electrodomesticos = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/div/div/div[1]/ul/li[3]")
            self.action.move_to_element(electrodomesticos).perform()#Hover
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/div/div/div[1]/ul/li[3]").click()#Click enlace
            
            #Validar Click en link "Electrodomesticos":
            assert self.driver.current_url=='https://shop.samsung.com/ar/linea-hogar?order=OrderByTopSaleDESC'
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div[2]/div/div/a").click()#Click Home (Sambsung)
        
        except WebDriverException as e:
            print("Event not Found")
            print(e)
        
        
        
        
        
        
    def tearDown(self):
        
        time.sleep(3)
        self.driver.quit()
        pass



if __name__ == '__main__':
    unittest.main()