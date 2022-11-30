from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml.html import fromstring
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import time
import shelve
import ctypes
import sys
import threading
import random
import webbrowser
from time import sleep
import pandas as pd


def main():
    df = pd.read_csv('Book.csv')
    print(df.to_string()) 
    # set up
    driver = webdriver.Chrome('chromedriver')# need to updatee chromedriver version
    driver.get("https://www.barnesandnoble.com") # Change depending on server
    wait = np.random.uniform(low=1.0, high=2.0, size=50)
    driver.find_element(by=By.XPATH, value='/html/body/div[2]/header/nav/div/div[3]/form/div/div[2]/div/input[1]').send_keys('Sarah')
    
    
if __name__ == "__main__":
    main()