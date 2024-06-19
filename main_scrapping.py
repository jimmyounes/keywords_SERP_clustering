from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from define_functions import * 


query="achter une baskete"    
get_urls_response_keywords(query,"fr","fr")


 