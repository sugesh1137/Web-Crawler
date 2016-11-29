import requests
from bs4 import BeautifulSoup

#import the basic module
#requests module is required to establish a successful connection between the python terminal and the working internet connection
#BeautifulSoup is used to extract the thus obtained raw data more flexibly

#first query, fetching the details of the mobile-phone section of the 1st page

def shopping_spider_query_1(keyword):
    url = 'https://www.olx.in/bangalore/' + keyword + '?/page=1'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('small',{'class':'breadcrumb small'}): #class of the title sction of the page, small is the attribute
        #href = link.get('span')
        key_word = item_name.span.string
            #print ('page no. ' + str(page))
            #print(href)
        print(key_word)


def shopping_spider_query_2(keyword2, page):
        url = 'https://www.olx.in/bangalore/' + keyword2 + '?/page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':'marginright5 link linkWithHash detailsLink'}):
            title = link.span.string #extracting string from the links obtained, binded within the attributes
            print ('page no. ' + str(page))
            #print(href)
            print(title)

shopping_spider_query_2('cars', 4)

#shopping_spider_query_1(mobilephones)

