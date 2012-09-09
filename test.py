import unittest
from selenium import webdriver

class SmokeTest(unittest.TestCase):
    def test_can_start_browser(self):
        driver = webdriver.Chrome()
        driver.get('http://www.google.com')
        self.assertEquals('Google', driver.title)
