import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import os
def scrape_info():
    #scraping news paragraph and title
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html=browser.html
    soup = bs(html, 'html.parser')
    result = soup.select_one("ul.item_list li.slide")
    title=result.find("div", class_= "content_title").get_text()
    news=result.find("div", class_ = "article_teaser_body").get_text()
    #scraping featured image url
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    urljpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(urljpl)
    html=browser.html
    soup = bs(html, 'html.parser')
    result=soup.find("div", class_ = "carousel_items")
    image=result.find("a", class_ = "button fancybox")
    link=(image['data-fancybox-href'])
    full_link=urljpl+link
    full_link
    #using pandas to get Mars facts
    url3="https://space-facts.com/mars/"
    tables = pd.read_html(url3)
    table1=tables[0]
    table2=tables[1]
    html_table1 = table1.to_html()
    html_table2=table2.to_html()
    #scraping 4 hemisphere urls
    url4="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url4)
    #Cerberus
    browser.visit(url4)
    html=browser.html
    soup = bs(html, 'html.parser')
    link= browser.links.find_by_partial_text("Cerberus")
    link.click()
    link2=browser.links.find_by_partial_text("Open")
    link2.click()
    html=browser.html
    soup = bs(html, 'html.parser')
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
    result= soup.find("img", class_= "wide-image")
    link_partial=result["src"]
    valles_marineris_link="https://astrogeology.usgs.gov"+link_partial
    # creating a dictionary
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    ]
    #Store data into dictionary?
    mars_data = {
        "title": title,
        "paragraph": news,
        "full_link": full_link,
        "html_table1": html_table1,
        "html_table2": html_table2,
        "hemisphere_image_urls": hemisphere_image_urls

    }

    return mars_data 