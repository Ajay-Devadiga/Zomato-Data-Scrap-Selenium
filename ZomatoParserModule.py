import json

import seleniumLoader
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


def getRestaurantList(region):
    chromeBrowser1 = seleniumLoader.chromeBrowser()
    driver = chromeBrowser1.driver
    driver.get('https://www.zomato.com/pune')
    sleep(3)
    # print(driver.page_source)
    print(driver.title)
    print(driver.current_url)

    inputelement = driver.find_element(By.CSS_SELECTOR, "div.sc-18n4g8v-0.gAhmYY input")
    inputelement.send_keys(region)
    print("typed")
    sleep(3)
    inputelement.click()
    print('searched')
    sleep(3)
    listElement = driver.find_element(By.CSS_SELECTOR, "div.sc-cLxPOX.sc-ekHBYt.cHAazR")
    listElement.click()
    print("choosed")
    # sleep(5)
    # url = driver.find_element(By.CSS_SELECTOR, "div.sc-bke1zw-1 a").get_attribute('href')
    # print('url', url)
    #
    # driver.get(regionUrl)

    sleep(5)
    delay = 10
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'root')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    y = 1000
    for timer in range(0, 50):
        print("scrolling... ", timer)
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        sleep(1)

    page_source = driver.page_source
    with open("zomato.html", "w", encoding="utf-8") as f:
        f.write(page_source)
    # print(html_text)
    soup = BeautifulSoup(page_source, "html.parser")
    child_soup = soup.find_all('script')
    scriptData = ""
    for i in child_soup:
        scripts = str(i.string)
        if ('"@type":"ItemList","itemListElement"' in scripts):
            scriptData = scripts
            print("Script: ", scriptData)
            print("###################")
            break
    # print(driver.page_source)
    x = json.loads(scriptData)

    restaurant_list = x['itemListElement']
    print(restaurant_list)
    json_object = json.dumps(x, indent=4)
    with open("restaurants.json", "w") as outfile:
        outfile.write(json_object)
    print(type(json_object))

    driver.quit()
    return restaurant_list



def navigateRestaurantPage(url):
    chromeBrowser1 = seleniumLoader.chromeBrowser()
    driver = chromeBrowser1.driver
    driver.get(url)

    y = 1000
    for timer in range(0, 5):
        print("scrolling... ", timer)
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        sleep(1)

    sleep(3)


# def getRestaurantList(regionUrl):
#     chromeBrowser2 = seleniumLoader.chromeBrowser()
#     driver = chromeBrowser2.driver
#     print("opening new")
