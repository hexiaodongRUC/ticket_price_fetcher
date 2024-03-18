# http_requests.py
import config
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_html_from_skyscanner():
    # Use Selenium to launch a browser and retrieve HTML content

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # Run Chrome in headless mode, i.e., without a GUI
    options.add_argument('--enable-javascript')
    #options.add_argument("user-agent=Your User Agent String")
    driver = webdriver.Chrome(options=options)  # You might need to specify the path to your Chrome driver executable  

    html_dict = {}    #save the htmls
    for dep in config.DEPARTURE:
       for des in config.DESTINATION:        
            price_list_html = f"https://www.skyscanner.com/transport/flights/{dep}/{des}/{config.DEPARTURE_TIME}/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false"
            driver.get(price_list_html)
            # Wait for the JavaScript content to fully load
            WebDriverWait(driver, 30)
            html = driver.page_source
            html_dict[f'{dep}-{des}'] = html
    driver.quit()  # Close the browser

    return html_dict

if __name__  == '__main__':
    get_html_from_skyscanner()