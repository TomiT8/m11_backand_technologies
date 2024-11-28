import time
from unittest import skip

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GuiTestWithSelenium(TestCase):

    @skip
    def test_home_page_edge(self):
        selenium_webdriver = webdriver.Edge()
        selenium_webdriver.get('http://127.0.0.1:8000/')
        time.sleep(2)
        assert 'Vítejte v naší HollyMovies filmové databázi.' in selenium_webdriver.page_source

    @skip
    def test_signup(self):
        selenium_webdriver = webdriver.Edge()
        selenium_webdriver.get('http://127.0.0.1:8000/accounts/signup/')
        time.sleep(2)
        username_field = selenium_webdriver.find_element(By.ID, 'id_username')
        username_field.send_keys('test_user2')
        time.sleep(2)
        first_name_field = selenium_webdriver.find_element(By.ID, 'id_first_name')
        first_name_field.send_keys('Test')
        time.sleep(2)
        last_name_field = selenium_webdriver.find_element(By.ID, 'id_last_name')
        last_name_field.send_keys('Test')
        time.sleep(2)
        email_field = selenium_webdriver.find_element(By.ID, 'id_email')
        email_field.send_keys('test@test.com')
        time.sleep(2)
        password1_field = selenium_webdriver.find_element(By.ID, 'id_password1')
        password1_field.send_keys('Test12345@')
        time.sleep(2)
        password2_field = selenium_webdriver.find_element(By.ID, 'id_password2')
        password2_field.send_keys('Test12345@')
        time.sleep(2)
        date_of_birth_field = selenium_webdriver.find_element(By.ID, 'id_date_of_birth')
        date_of_birth_field.send_keys('02-05-1990')
        time.sleep(2)
        biography_field = selenium_webdriver.find_element(By.ID, 'id_biography')
        biography_field.send_keys('Test biografie.')
        time.sleep(2)

        submit_button = selenium_webdriver.find_element(By.ID, 'id_submit')
        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)

        # assert 'Vítejte v naší HollyMovies filmové databázi.' in selenium_webdriver.page_source
        assert 'A user with that username already exists.' in selenium_webdriver.page_source

    def test_movie_not_in_db(self):
        selenium_webdriver = webdriver.Edge()
        selenium_webdriver.get('http://127.0.0.1:8000/movie/1000/')
        time.sleep(2)
        assert 'Katalog filmů' in selenium_webdriver.page_source