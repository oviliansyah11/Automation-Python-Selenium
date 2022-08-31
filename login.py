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
    driver.get("http://myappventure.herokuapp.com/login")
    yield driver
    driver.quit()


def test_login_invalid_email_password(driver):
    email = driver.find_element(By.NAME, 'email')
    email.send_keys(fake.email())

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(fake.aba())

    btnlogin = driver.find_element(
        By.XPATH, "//button[contains(text(),'Masuk')]")
    btnlogin.click()

    sleep(3)

    expMessage = 'Alamat email atau kata sandi yang\nanda masukan tidak valid'
    actMessage = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[2]/p[1]").text

    assert expMessage in actMessage


def test_login_valid_email_invalid_password(driver):
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('test@test.com')

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(fake.aba())

    btnlogin = driver.find_element(
        By.XPATH, "//button[contains(text(),'Masuk')]")
    btnlogin.click()

    sleep(3)

    expMessage = 'Kata Sandi Salah '
    actMessage = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[2]/p[1]").text

    assert expMessage in actMessage


def test_login_valid_email_password(driver):
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('test@test.com')

    password = driver.find_element(By.NAME, 'password')
    password.send_keys('12345678')

    btnlogin = driver.find_element(
        By.XPATH, "//button[contains(text(),'Masuk')]")
    btnlogin.click()

    sleep(10)

    expTitle = 'Home - My Appventure'
    actTitle = driver.title

    assert expTitle == actTitle
