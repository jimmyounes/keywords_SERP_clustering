from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from define_functions import * 


keywords=["achter une baskete","chute de cheveux","cheveux lisse","cheveux blanc"]    
print(get_urls_for_keywords(keywords,"fr","fr"))


 