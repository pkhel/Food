from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
def setup_function(function):
    driver.get("https://www.guru99.com/")
    driver.maximize_window()
    print("setup")
def teardown_function(function):
    print("teardown")
def test_first():
    print(driver.execute_script('return document.URL'))
def test_second():
    print(driver.execute_script('return document.title'))







