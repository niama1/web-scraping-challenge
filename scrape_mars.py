# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
from bs4 import BeautifulSoup 
import os
from splinter import Browser
import pandas as pd


# %%
import selenium


# %%
# URL of page to be scraped
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# %%
get_ipython().system(u'which chromedriver')


# %%
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}


# %%
browser = Browser('chrome', **executable_path)


# %%
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# %%
browser.is_element_not_present_by_css('.article_teaser_body', wait_time=5)


# %%
#using bs to write it into html
html = browser.html
soup = BeautifulSoup(html,"html.parser")


# %%
print(soup)


# %%
news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")


# %%
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/'
browser.visit(featured_image_url)


# %%
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# %%
featured_img_url_raw = soup.find("div", class_="carousel_items").find("article")["style"]
featured_img_url = featured_img_url_raw.split("'")[1]
featured_img_url = featured_img_url + featured_img_url
featured_img_url


# %%
weather_twitter_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_twitter_url)


# %%
browser.is_element_not_present_by_css('.css-1dbjc4n', wait_time=5)


# %%
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# %%
outer_tweet = soup.find('div', attrs = {'class': 'css-1dbjc4n'})
print(outer_tweet)


# %%
import pandas as pd
df = pd.read_html('https://space-facts.com/mars/')[0]
# print(df)
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url) 


# %%
hemisphere_image_urls = []

# First get a list of all the hemispheres
links = browser.find_by_css('a.product-item h3')
for item in range(len(links)):
    hemisphere = {}
    
    # We have to find the element on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item h3')[item].click()
    
    # Get hemisphere title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # Next we find the Sample Image anchor tags and extract the href
    sample_element = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_element['href']
    
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
    # Finally we navigate backwards
    browser.back()


# %%
hemisphere_image_urls


# %%



