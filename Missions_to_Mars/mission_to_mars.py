from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd

executable_path = {"executable_path":"C:/Users/azrea/Desktop/Class Stuff/chromedriver"}
browser = Browser("chrome", **executable_path, headless = False)

mars_site_url = "https://redplanetscience.com/"
browser.visit(mars_site_url)

response = requests.get(mars_site_url)

soup = bs(response.text, "lxml")

news_title = soup.find('div', class_="content_title").get_text()

news_para = soup.find('div', class_="article_teaser_body").get_text()

print(news_title)
print(news_para)

image_url = "https://spaceimages-mars.com/image/featured/mars3.jpg"
browser.visit(image_url)


url = "https://space-facts.com/mars/"
browser.visit(url)

tables = pd.read_html(url)

mars_df = tables[0]
mars_df


mars_url='https://marshemispheres.com/'
browser.visit(mars_url)
html=browser.html
soup=bs(html,'html.parser')


mars_hemi=soup.find('div',class_='collapsible results')
mars_item=mars_hemi.find_all('div',class_='item')
hemisphere_image_urls=[]

for item in mars_item:
    try:
        hemi=item.find('div',class_='description')
        title=hemi.h3.text
        hemi_url=hemi.a['href']
        browser.visit(mars_url+hemi_url)
        html=browser.html
        soup=bs(html,'html.parser')
        image_src=soup.find('li').a['href']
        if (title and image_src):
            print('-'*50)
            print(title)
            print(image_src)
        hemi_dict={
            'title':title,
            'image_url':image_src
        }
        hemisphere_image_urls.append(hemi_dict)
    except Exception as e:
        print(e)

mars_dictionary={
    "news_title":news_title,
    "news_para":news_para,
    "image_url":image_url,
    "fact_table":tables,
    "hemisphere_images":hemisphere_image_urls
}

mars_dictionary
