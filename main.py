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

class PyVideoDownloader:

    def __init__(self,url):
        self.website_url = url
        self.movie_download_links_dict = dict()
        self.page_scrape()

    def init(self):
        print("****** Download Helper ******")
        self.website_url = input("Enter the base url of the website you would like to download from:\n")
        if self.url_validator() != True :
            print("** You entered an invalid URL **")
            return
        self.page_scrape()

    def url_validator(self):
        url_regex = re.compile(r"^(?:http)s?://(www)?[a-z0-9./?=\"_:]*", re.IGNORECASE | re.MULTILINE)
        if re.match(url_regex,self.website_url) is not None:
            return True
        else :
            return False

    def page_scrape(self):
        url_opener = URLopener()
        try:
            parent_page = url_opener.open(self.website_url)
            parent_page_soup = BeautifulSoup(parent_page,'html.parser')
            available_movie_seasons = parent_page_soup.select(".data > a")
            print(str.format("Movie Title : {0}",parent_page_soup.title.string.strip()))
            print(str.format("Available Seasons : {0}",len(available_movie_seasons)))
            available_movie_seasons_links = [season_link.get("href") for season_link in available_movie_seasons]
            index = -1
            for season_link in range(0,len(available_movie_seasons)):
                self.scrap_child_pages(available_movie_seasons_links[index],str.format("Season {0}",season_link+1))
                index -= 1
            self.display_available_download()
        except Exception as e:
            print(e)
    
    def scrap_child_pages(self,page_url,current_season):
        url_opener = URLopener()
        try:
            page = url_opener.open(page_url)
            page_soup = BeautifulSoup(page,'html.parser')
            available_episodes = page_soup.select(".data > a")
            available_episodes = [ episode_link.get("href") for episode_link in available_episodes ] 
            self.movie_download_links_dict[current_season] = available_episodes
        except Exception as e:
            print(e)

    def display_available_download(self):
        print(self.movie_download_links_dict)

py_downloader = PyVideoDownloader("http://o2tvseries.com/Mr-Robot-9/index.html")