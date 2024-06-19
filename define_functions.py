from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def getElement(typeBalise,identifier,driver):
    try: 
        element=WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"{typeBalise}[{identifier}]"))
        )
        return element
    except Exception as e:
        print("Error exception ", e)

def button_click(typeBalise,identifier,driver):
    button=getElement(typeBalise,identifier,driver)
    button.click()

def create_driver():
    service = webdriver.ChromeService(executable_path='chromedriver.exe')
    options = webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')  
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')  
    return webdriver.Chrome(service=service, options=chrome_options)

def get_urls_response_keywords(query,language,country):

    urls=[] 
    url=f"https://www.google.com/search?q={query}&gl={language}&hl={country}"
    driver = create_driver()
    driver.get(url)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    td_elements = soup.find('div', {'id': "search"})
    button_click("button","id='L2AGLb'",driver) 
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    td_elements = soup.find('div', {'id': "search"})
    elements = soup.find_all('div', class_="MjjYud") 
    for element in elements :
        soup = BeautifulSoup(str(element), 'html.parser') 
        url=soup.find('cite', class_="qLRx3b tjvcx GvPZzd cHaqb")
        if(url!=None):
            url=url.get_text().split(" ›")
            if(url not in urls):urls.append(url[0])
    print(urls)
    driver.quit()        
