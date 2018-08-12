"""

By : code_blooded Twitter: @_emmarex_
Just a simple python file to help me download series i love
from O2tvseries

Sunday 12th August 2018

"""
import urllib
import re

def init():
    print("****** Download Helper ******")
    website_url = input("Enter the base url of the website you would like to download from:\n")
    if url_validator(website_url) != True :
        print("** You entered an invalid URL **")
        return
    page_scrape(website_url)

def page_scrape(page_url):
    parent_page =  urllib.request.urlopen(page_url)

def url_validator(url):
    url_regex = re.compile(r"^(?:http)s?://(www)?[a-z0-9./?=\"_:]*", re.IGNORECASE | re.MULTILINE)
    if re.match(url_regex,url) is not None:
        return True
    else :
        return False

init()