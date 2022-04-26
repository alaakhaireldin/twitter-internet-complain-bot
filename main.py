import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = "C:\Development\chromedriver.exe"
PROMISED_DOWN = 150
PROMISED_UP = 10
username = os.environ.get("TWITTER_USERNAME")
password = os.environ.get("TWITTER_PASSWORD")
test_speed = 'https://www.speedtest.net/result/13077629267'
twitter_link = 'https://twitter.com/home?lang=en'
