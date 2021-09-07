# import dependancies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# write a function that will execute all of your scraping code 
def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False) 

    # Visit the URL https://redplanetscience.com
    url - "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(3)

    # scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Get the news title and paragraph
    news_elements = soup.find_all('div', class_ = 'list_text')
    # Loop through the results to find news title and paragraph
    for news_element in news_elements:
        news_titles = news_element.find('div', class_ = 'content_title')
        news_p = news_element.find('div', class_ = 'article_teaser_body')
    
    # JPL Mars Spave Images: visit url: 'https://spaceimages-mars.com'
    url = 'https://spaceimages-mars.com/'
    broswer.visit(url)

    # pull html into Beautiful Soup parser  
    html=browser.html
    soup=bs(html, 'html.parser')

    # find the url of the fuatured images
    image = soup.find('img', class_ = 'headerimage fade-in')['src']
    featured_imge_url = url + image

    # Mars Facts: Visit the url: 'https://galaxyfacts-mars.com/'
    # vist the url to get Mars facts and scrape the table 
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # pull html into beautiful Soup parser
    html = browser.html
    soup = (html, 'html.parser')

    # scrape the table content about Mars facts including Diameters, Mass, etc
    # use Panda's 'read_html' to parse the url and convert the html to string
    tables= pd.read_html(url)
    # store data in DataFrame
    table_df = tables[0]
    table_df.columns = ['Mars-Earth Comparision', 'Mars', 'Earth']
    table_df = table_df.iloc[1:]

    # Mars Hemispheres: visit the URL: 'https://marshemispheres.com/'
    # obtain high resolution images for each of Mar's hemispheres
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # pull html into Beautiful Soup parser
    html=browser.html
    soup=bs(html, 'html.parser')

    # find the high resolution images url and title of each Hemisphere
    high_reso_image = soup.find_all('div', class_ = 'description')
    # loop thru the list to retrive image url and title
    for image in high_reso_image:
        #     title of the image
        image_title = image.find('h3').get_text()
        #     find image url
        img_url = image.find('a', class_ = 'itemLink product-item')['href']
        hemis_url = url + img_url
        #     now find the high resolution image from 'hemis_url'
        browser.visit(hemis_url)
        html = browser.html
        soup = bs(html,'html.parser')
        img_src = soup.find('img', class_='wide-image')['src']
        highresol_imgurl = url + img_src

        # store data in a dictionary
        hemisphere_image_urls = {
            "title": image_title,
            "img_url": highresol_imgurl
        }

        # close the browser after scraping
        browser.quit()

        # create disctionary for all the data from above
        mars_information = {
            "news_title": news_titles.text,
            "news_p": news_p.text,
            "featured_imge_url": featured_imge_url,
            "facts_table": table_df,
            "hemispheres": hemisphere_image_urls
        }
        # return results
        return mars_information



    