### Web Scraping Homework (Week 12 HW) - Mission to Mars

Mission: Build a web application that scrapes various websites for data related to Mars and display the information in a single HTML page.\
This data includes: latest mars news, current featured image, a table of mars facts, and various images of mars hemisperes.

This project contains:
- A Jupyter Notebook containing the scraping code
- Two python.py files
    - Scrape_mars.py executes the scraping code & stores results in a dictionary
    - app.py puts this data in a mongo database using flask and then links it to the index.html document to create the "website"
- An index.html file for the created "website" that will execute the script to scrape new data when a button at the top of the page is clicked
- Screenshots of the final web application after it has been run

**Scraped Sites:**\
[NASA Mars News Site](https://mars.nasa.gov/news/)\
[JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)\
[Mars Facts](https://space-facts.com/mars/)\
[USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

### Final Site Screencapture
![MarsPage](https://github.com/SarahZ22/Project_1_Tremors_Analysis/blob/master/Site_Screenshots/Top_Site_SC.PNG)
