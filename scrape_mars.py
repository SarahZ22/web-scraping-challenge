# Step 2 - MongoDB and Flask Application
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. Convert your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
import requests

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # NASA Mars News
    # Define and retrieve the page
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    #Scrape to get title and text
    news_title = soup.find("li", class_="slide").find("div", class_="content_title").text
    news_p = soup.find("li", class_="slide").find("div", class_="article_teaser_body").text

    # JPL Mars Space Images - Featured Image
    # Define and retrieve the page
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    # Navigate site and save full size url string of image to variable
    browser.click_link_by_partial_text("FULL IMAGE")
    browser.click_link_by_partial_text("more info")
    html = browser.html
    soup = bs(html, "html.parser")
    # Scrape for full image 
    base_url = "https://www.jpl.nasa.gov"
    img_url = soup.find('figure', class_='lede').find('a').find('img')['src']
    # Add image url to base url
    featured_image_url = base_url + img_url

    # Mars Facts
    # Have pandas read any tables on mars facts page
    facts_url = 'https://space-facts.com/mars/'
    fact_table = pd.read_html(facts_url)
    # Filter to table I want to work with
    fact_df = fact_table[0]
    # Rename columns
    fact_df.columns = ["Description", "Mars"]
    # Remove Index/set new
    facts = fact_df.set_index("Description")
    # Convert to html string & clean
    html_facts = facts.to_html()
    html_facts = html_facts.replace('\n', '')

    # Mars Hemispheres
    # Define and retrieve the page
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    html = browser.html
    soup = bs(html, "html.parser")
    # Blank list to contain the dictionaries
    hemisphere_image_urls = []
    # Base image url
    baseimg_url="https://astrogeology.usgs.gov/"
    # Soup object
    hemis = soup.find_all('div', class_='item')
    # Loop to get each title & url
    for hemi in hemis:
        title = hemi.find('h3').text
        browser.click_link_by_partial_text("Hemisphere Enhanced")
        img_html = browser.html
        img_soup = bs(img_html, "html.parser")
        imgs_url = img_soup.find("img", class_="wide-image")["src"]
        image_url = baseimg_url+imgs_url
        hemisphere_image_urls.append({"title": title, "img_url": image_url})

    # Close the browser after scraping
    browser.quit() 

    # Dictionary with all scraped info
    mars_dict={
    "Mars_news_headline": news_title,
    "Mars_news_p": news_p,
    "Featured_mars_image": featured_image_url,
    "Mars_facts": html_facts,
    "Mars_hemispheres": hemisphere_image_urls
    }
    return mars_dict

if __name__ == "__main__":
    data = scrape()
    print(data)