import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from google_page import GooglePage


class GoogleTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= r'C:\chrome-driver\chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Emi Ciappi')

        self.assertEqual('Emi Ciappi', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)