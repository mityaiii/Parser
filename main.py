import imp
import requests
import lxml
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def createFileHtml(url, header):
    req = requests.get(url, headers=header)
    src = req.text
    with open("index.html", "w",  encoding="utf-8") as file:
        file.write(src)

def getArticles (nameOfFile, nameOfProperty):
    with open(nameOfFile, "r", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    propertyHtml = soup.find_all(class_="property-value")
    titleOfProductsHtml = soup.find_all(class_="property-title")
    property = []
    for i in range(len(titleOfProductsHtml)):
        item_text = titleOfProductsHtml[i].text
        if item_text == nameOfProperty:
            property.append(propertyHtml[i].text)
    print(property)

def сheckAvailability(url):
    driver = webdriver.Chrome(executable_path='D:/VS_Projects/normalParsing/chromedriver_win32/chromedriver.exe')
    try:  
        driver.get(url=url)
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        element = driver.find_element(By.CLASS_NAME, 'check-availability-block')
        element.click()
        time.sleep(3)
    except Exception as ex:
        print(ex)   
    finally:
        driver.close()
        driver.quit()     



def main():

    header = {
        'accept' : '*/*',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    url = 'https://fix-price.com/catalog/dlya-doma/p-5036106-podstavka-kuhonnaya-uglovaya-itchen'
    
    сheckAvailability(url)

    # print(articleOfProduct)


if __name__ == '__main__':
    main()