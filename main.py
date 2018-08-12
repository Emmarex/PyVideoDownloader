"""

By : code_blooded Twitter: @_emmarex_
Just a simple python file to help me download series i love
from O2tvseries

Sunday 12th August 2018

"""
import urllib.request
import re
from bs4 import BeautifulSoup
from url_opener import URLopener

def init():
    print("****** Download Helper ******")
    website_url = input("Enter the base url of the website you would like to download from:\n")
    if url_validator(website_url) != True :
        print("** You entered an invalid URL **")
        return
    page_scrape(website_url)

def url_validator(url):
    url_regex = re.compile(r"^(?:http)s?://(www)?[a-z0-9./?=\"_:]*", re.IGNORECASE | re.MULTILINE)
    if re.match(url_regex,url) is not None:
        return True
    else :
        return False

def page_scrape(page_url):
    url_opener = URLopener()
    try:
        parent_page = url_opener.open(page_url)
        parent_page_soup = BeautifulSoup(parent_page,'html.parser')
        available_movie_seasons = parent_page_soup.select(".data > a")
        print(str.format("Movie Title : {0}",parent_page_soup.title.string.strip()))
        print(str.format("Available Seasons : {0}",len(available_movie_seasons)))
        available_movie_seasons_links = [season_link.get("href") for season_link in available_movie_seasons]
        index = -1
        for season_link in range(0,len(available_movie_seasons)):
            scrap_and_download(available_movie_seasons_links[index],season_link+1)
            index -= 1
    except Exception as e:
        print(e)

def scrap_and_download(page_url,index):
    url_opener = URLopener()
    try:
        page = url_opener.open(page_url)
        page_soup = BeautifulSoup(page,'html.parser')
        print(page_soup.select(".data > a"))
    except Exception as e:
        print(e)
    print(str.format("*** Downloading Season {0}",index))

def scrap_and_download(page_url,index):
    print(str.format("Downloading Season {0}",index))

page_scrape("http://o2tvseries.com/Mr-Robot-9/index.html")