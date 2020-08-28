import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import os
import datetime as dt
import time


def home():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape_all():

    browser = home()

    title, news = scrape_news()

    #Run all other functions 
    mars_data = {
        "title": title,
        "paragraph": news,
        "main_image": scrape_main_image(),
        "html_table1": mars_table(),
        "hemisphere_image_urls": mars_hemis()
    }

    browser.quit()

    return mars_data


def scrape_news():

    browser = home()


    #scraping news paragraph and title
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html=browser.html
    soup = bs(html, 'html.parser')
    result = soup.select_one("ul.item_list li.slide")

    try:
        title=result.find("div", class_= "content_title").get_text()
        news=result.find("div", class_ = "article_teaser_body").get_text()

    except AttributeError:
        return None, None
    
    browser.quit()

    return title, news

def scrape_main_image():
    browser = home()
    
    urljpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(urljpl)

    time.sleep(1)

    html=browser.html
    soup = bs(html, 'html.parser')
    try:
        result=soup.find("div", class_ = "carousel_items")
        image=result.find("a", class_ = "button fancybox")
        link=(image['data-fancybox-href'])
        full_link="https://www.jpl.nasa.gov/"+link
    except AttributeError:
        return None
    

    browser.quit()

    return full_link

def mars_table():

    browser = home()

    #using pandas to get Mars facts
    url3="https://space-facts.com/mars/"
    tables = pd.read_html(url3)
    table1=tables[0]
    table1=table1.set_index(0)
    table1.index.name = 'Description'
    table1.columns = ['Mars']
    html_table1 = table1.to_html()
    


    browser.quit()

    return html_table1

def mars_hemis():

    browser = home()
    #scraping 4 hemisphere urls
    url4="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url4)
    browser.visit(url4)
    html=browser.html
    soup = bs(html, 'html.parser')
    link= browser.links.find_by_partial_text("Cerberus")
    link.click()
    link2=browser.links.find_by_partial_text("Open")
    link2.click()
    html=browser.html
    soup = bs(html, 'html.parser')
    cerberus_title = browser.find_by_tag('h2').text.replace(" Enhanced", "")
    result= soup.find("img", class_= "wide-image")
    link_partial=result["src"]
    cerberus_link="https://astrogeology.usgs.gov"+link_partial
    # Schiaparelli
    browser.visit(url4)
    html=browser.html
    soup = bs(html, 'html.parser')
    link= browser.links.find_by_partial_text("Schiaparelli")
    link.click()
    link2=browser.links.find_by_partial_text("Open")
    link2.click()
    html=browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_title = browser.find_by_tag('h2').text.replace(" Enhanced", "")
    result= soup.find("img", class_= "wide-image")
    link_partial=result["src"]
    schiaparelli_link="https://astrogeology.usgs.gov"+link_partial
    # Syrtis Major
    browser.visit(url4)
    html=browser.html
    soup = bs(html, 'html.parser')
    link= browser.links.find_by_partial_text("Syrtis Major")
    link.click()
    link2=browser.links.find_by_partial_text("Open")
    link2.click()
    html=browser.html
    soup = bs(html, 'html.parser')
    syrtis_major_title = browser.find_by_tag('h2').text.replace(" Enhanced", "")
    result= soup.find("img", class_= "wide-image")
    link_partial=result["src"]
    syrtis_major_link="https://astrogeology.usgs.gov"+link_partial
    # Valles Marineris
    browser.visit(url4)
    html=browser.html
    soup = bs(html, 'html.parser')
    link= browser.links.find_by_partial_text("Valles Marineris")
    link.click()
    link2=browser.links.find_by_partial_text("Open")
    link2.click()
    html=browser.html
    soup = bs(html, 'html.parser')
    valles_marineris_title = browser.find_by_tag('h2').text.replace(" Enhanced", "")
    result= soup.find("img", class_= "wide-image")
    link_partial=result["src"]
    valles_marineris_link="https://astrogeology.usgs.gov"+link_partial
    # creating a dictionary
    hemisphere_image_urls = [
        {"title": valles_marineris_title, "img_url": valles_marineris_link},
        {"title": cerberus_title, "img_url": cerberus_link},
        {"title": schiaparelli_title, "img_url": schiaparelli_link},
        {"title": syrtis_major_title, "img_url": syrtis_major_link},
    ]
    
    browser.quit()

    return hemisphere_image_urls 