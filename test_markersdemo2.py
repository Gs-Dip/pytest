# markers ar inbuild decorator ar bebohar--------------

# import pytest #markers bebohar korar jonno obossoi pytest import kore nite hobe
# import sys
# @pytest.mark.skip #skip hocche markers ar akta decoretor
# def test_login():
#     print("Login done")

# @pytest.mark.skipif(sys.version_info<(3,9),reason="python verson not supported") #jodi  (sys.version_info<(3,8),reason="python verson not supported") ai condition ta match kore taholei sudhu aitake skip korbe....akhane sys.version_info diye python ar version ke bojhano hoyeche....amar python version hocche 3.8.18 jehetu aita 3.9 ar theke choto tai ai condition ta true hobe and ai tastcase ke skip korbe and reason ar value ta messege aakare dekhabe
# def test_addproduct():
#     print("add product")   

# @pytest.mark.xfail # xfail decoretor tokhoni bebohar kora hobe jokhon amra jani je amader code a bug ache aita fail o hoite  pare pass o hoite pare tokhon xfail bebohar korbo....jodi pass hoi tahole xpass dekhabe jodi fail hoy xfail dekhabe  
# def test_logout():
#     assert False
#     print("logout done") 


# def test_closeapplication():
#     assert True
#     print("close the application")




#----------------markers ar peramiterize decoretor ar bebohar-------------------------

import pytest #markers bebohar korar jonno obossoi pytest import kore nite hobe

import sys

@pytest.mark.parametrize("username,password",[
    ("selenium","webdriver"),
    ("python","pytest"),
    ("dip","dip123")
]) # parametrize(ar moddhe argument and list pass kora jai).....aitar maddhome api test automation test mobile test kora jai
def test_login(username,password):
    print(username)
    print(password)
     