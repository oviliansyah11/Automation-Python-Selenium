import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from faker import Faker

fake = Faker('id_ID')


@pytest.fixture
def driver():
    s = Service(
        'C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("http://myappventure.herokuapp.com/registration")
    yield driver
    driver.quit()


def test_check_fields(driver):
    btnDaftar = driver.find_element(
        By.XPATH, "//button[contains(text(),'Daftar sekarang')]")
    btnDaftar.click()
    sleep(2)

    expectedUsername = "diperlukan username"
    expectedEmail = "diperlukan email"
    expectedPassword = "diperlukan kata sandi"
    actualUsername = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[2]/div[1]").text
    actualEmail = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[3]/div[1]").text
    actualpassword = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]").text

    sleep(2)
    assert actualUsername == expectedUsername
    assert actualEmail == expectedEmail
    assert actualpassword == expectedPassword


def test_input_username(driver):
    username = driver.find_element(By.NAME, 'username')
    username.send_keys(fake.first_name())

    btnDaftar = driver.find_element(
        By.XPATH, "//button[contains(text(),'Daftar sekarang')]")
    btnDaftar.click()

    expectedEmail = "diperlukan email"
    expectedPassword = "diperlukan kata sandi"
    actualEmail = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[3]/div[1]").text
    actualpassword = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]").text

    sleep(2)
    assert actualEmail == expectedEmail
    assert actualpassword == expectedPassword


def test_input_username_email(driver):
    username = driver.find_element(By.NAME, 'username')
    username.send_keys(fake.first_name())

    email = driver.find_element(By.NAME, 'email')
    email.send_keys(fake.email())

    btnDaftar = driver.find_element(
        By.XPATH, "//button[contains(text(),'Daftar sekarang')]")
    btnDaftar.click()

    expectedPassword = "diperlukan kata sandi"
    actualpassword = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[4]/div[1]").text

    sleep(2)
    assert actualpassword == expectedPassword


def test_registration(driver):
    username = driver.find_element(By.NAME, 'username')
    username.send_keys(fake.first_name())

    email = driver.find_element(By.NAME, 'email')
    email.send_keys(fake.email())

    password = driver.find_element(By.NAME, 'password')
    password.send_keys("12345678")

    btnDaftar = driver.find_element(
        By.XPATH, "//button[contains(text(),'Daftar sekarang')]")
    btnDaftar.click()

    sleep(2)

    expectedResult = "Selamat! Akun anda berhasil dibuat"
    actualResult = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[2]/p[1]").text

    assert actualResult == expectedResult
