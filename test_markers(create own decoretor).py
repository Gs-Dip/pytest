import pytest #markers bebohar korar jonno obossoi pytest import kore nite hobe

@pytest.mark.smoke # akhane ami smoke name akta nijesho ba own decoretor create  korechi
def test_login():
    print("Login done")

@pytest.mark.regression
def test_addproduct():
    print("add product")   

@pytest.mark.smoke
def test_logout():
    print("Logout done")      