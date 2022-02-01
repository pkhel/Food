import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

@pytest.fixture(scope="function")
def before():
    driver.get("https://www.guru99.com/")
    driver.maximize_window()
    print("setup")
    yield
    print("teardown")


def test_first(before):
    print(driver.execute_script('return document.URL'))


def test_second(before):
    print(driver.execute_script('return document.title'))
