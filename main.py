"""

Just a simple python file to help me download series i love
from O2tvseries

Sunday 12th August 2018

"""
import urllib.request
import re
from bs4 import BeautifulSoup
from url_opener import URLopener

class PyVideoDownloader:

    def __init__(self):
        self.website_url = ""
        self.movie_download_links_dict = dict()
        self.movie_title = ""
        self.init()

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
            self.movie_title = parent_page_soup.title.string.replace(" ","").strip()
            print(str.format("Movie Title : {0}",self.movie_title))
            print(str.format("Available Seasons : {0}",len(available_movie_seasons)))
            print("Please wait")
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
            season_episodes_download_link = [ self.fetch_download_link_from_page(available_episode) for available_episode in available_episodes]
            # ----
            self.movie_download_links_dict[current_season] = season_episodes_download_link
        except Exception as e:
            print(e)

    def fetch_download_link_from_page(self,current_page_url):
        url_opener = URLopener()
        try:
            return_data = dict()
            page = url_opener.open(current_page_url)
            soup = BeautifulSoup(page,'html.parser')
            download_link = soup.select_one(".data > a")
            return_data[download_link.getText()] = download_link.get("href")
            return return_data
        except Exception as e:
            print(e)

    def display_available_download(self):
        # print(self.movie_download_links_dict)
        filename = str.format("download_links/{0}_download_links.txt",self.movie_title.replace(".","").strip())
        links_file = open(filename,"w+")
        links_file.write(str(self.movie_download_links_dict))
        links_file.close()
        print(str.format("Done !! File saved as {0}",filename))

py_downloader = PyVideoDownloader()
