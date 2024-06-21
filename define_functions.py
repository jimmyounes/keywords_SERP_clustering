from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import undetected_chromedriver as uc

def getElement(typeBalise,identifier,driver):
    try: 
        element=WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"{typeBalise}[{identifier}]"))
        )
        return element
    except Exception as e:
        print("Error exception ", e)

def button_click(typeBalise,identifier,driver):
    button=getElement(typeBalise,identifier,driver)
    
    button.click()

def create_driver():
    
    ua = UserAgent()
    user_agent = ua.random
    service = webdriver.ChromeService(executable_path='chromedriver.exe')
    options = webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument('--start-maximized')  
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    proxy_address = "http://51.254.78.223:80"
    #options.add_argument(f'--proxy-server={proxy_address}')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
    chrome_options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #chrome_options.add_argument('--headless')  
    
    return uc.Chrome()
    return webdriver.Chrome(service=service, options=chrome_options)
    
    #
   
def get_urls_response_keywords(query,language,country):
    
    urls=[] 
    url=f"https://www.google.com/search?q={query}&gl={language}&hl={country}"
    driver = create_driver()
    driver.get(url)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    td_elements = soup.find('div', {'id': "search"})
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    
    button_click("button","id='L2AGLb'",driver) 
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    td_elements = soup.find('div', {'id': "search"})
    elements = soup.find_all('div', class_="MjjYud") 
    for element in elements :
        soup = BeautifulSoup(str(element), 'html.parser') 
        url_element=soup.find('a',{"jsname":"UWckNb"})

        if(url_element!=None):
            url=url_element.get('href')
            if(url not in urls):urls.append(url)
    driver.quit()        
    return urls

def get_urls_from_html(driver,button_cookies):
    urls=[]
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    if(button_cookies==True):
        button_click("button","id='L2AGLb'",driver) 
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all('div', class_="MjjYud") 
    for element in elements :
        soup = BeautifulSoup(str(element), 'html.parser') 
        url_element=soup.find('a',{"jsname":"UWckNb"})
        if(url_element!=None):
            url=url_element.get('href')
            if(url not in urls):urls.append(url)
    return urls 

def connexion(driver):
    driver.get("https://www.google.fr")
    time.sleep(10)
    button_click("button","id='L2AGLb'",driver) 
    time.sleep(10)
    button_click("a","class='gb_Ea gb_wd gb_nd gb_ne'",driver)
    time.sleep(2)
    input=getElement("input","type='email'",driver)
    emails=["jimmyouyounes","jimmyyounes11@gmail.com"]
    email="jimmyyounes11@gmail.com"
    for character in email : 
        input.send_keys(character)
        time.sleep(1)
    
    button_click("button","class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b'",driver)
    time.sleep(5)
    input=getElement("input","type='password'",driver) 
    password="*****"
    for character in password : 
        input.send_keys(character)
        time.sleep(0.05)
    button_click("button","class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b'",driver)
     

def init_prepare_google():     
    driver = create_driver()
    time.sleep(120)
    urls=[] 
    connexion(driver)
    return driver

def get_urls_for_keywords(keywords,language,country):
    keyword_urls={}
    
    #driver = init_prepare_google()
    driver = create_driver()
    time.sleep(30)
    url=f"https://www.google.com/search?q={keywords[0]}&gl={language}&hl={country}"
    driver.get(url)
    urls=get_urls_from_html(driver,True)
    keyword_urls[keywords[0]]=urls
    i=0
    for keyword in keywords[1:]:
        
            input=getElement("textarea","class='gLFyf'",driver)
            input.clear()
            input.send_keys(keyword)    
            input.send_keys(Keys.ENTER)
            time.sleep(0.05)
            urls=get_urls_from_html(driver,False)
            keyword_urls[keyword]=urls
            i=i+1
            time.sleep(2)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            if(i%5==0):time.sleep(3)
        
    driver.quit()   
       
    return keyword_urls
   
#0.1
