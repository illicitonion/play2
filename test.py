import os
import unittest
from selenium import webdriver

class SmokeTest(unittest.TestCase):
    def test_can_start_browser(self):
        driver = webdriver.Chrome(executable_path=os.path.abspath('./chromedriver_linux32'))
        driver.get('http://www.google.com')
        self.assertEquals('Google', driver.title)
