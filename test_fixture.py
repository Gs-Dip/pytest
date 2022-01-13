# import pytest # fixture bebohar korar jonno pytest import korte hobe

# @pytest.fixture
# def setup(): #akhane setup name akta fixture create kora hoyeche jeta kono test ar aage exicute hobe 
#     print("start Browser")

#     yield # yield ar maddhome amra je kajti korbo ta test ar pore exicute hobe 
#     print("close Browser") 



# def test_1(setup):
#    print("test 1 executed")


# def test_2(setup):
#    print("test 2 executed")


# def test_3(setup):
#    print("test 3 executed")      




####-----------------------another use of fixture----------------


import pytest # fixture bebohar korar jonno pytest import korte hobe
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver=None # ak ak somoy akta url get korar jonno akhane drive=None deya hoyeche
@pytest.fixture
def setup(): #akhane setup name akta fixture create kora hoyeche jeta kono test ar aage exicute hobe 
    print("start Browser")
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  

    yield # yield ar maddhome amra je kajti korbo ta test ar pore exicute hobe 
    driver.quit()
    print("close Browser") 



def test_1(setup):
   driver.get("http://www.facebook.com")
   print("test 1 executed")


def test_2(setup):
   driver.get("http://www.google.com") 
   print("test 2 executed")


def test_3(setup):
   driver.get("http://www.gmail.com") 
   print("test 3 executed")  