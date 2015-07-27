__author__ = 'zero'

import urllib
import urllib2
from bs4 import BeautifulSoup
#from comicreader.models import *

def crawlCategory():
    """
    crawl only category of http://blogtruyen.com
    :return: list all category
    """
    print "----->  crawlCategory()"
    html = urllib.urlopen("http://blogtruyen.com/danhsach/tatca")
    soup = BeautifulSoup(html.read())
    ulCategory = soup.findAll('ul', {'class':'submenu category'})
    liCategory = ulCategory[0].findAll('li')
    listCategory = []
    for element in liCategory:
        listCategory.append(element.text)
        print element.text

    return listCategory

def maxPage():
    """
    find max page
    :return: max page
    """
    URL = "http://blogtruyen.com/ListStory/GetListStory"
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    data = urllib.urlencode({'Url' : 'tatca', 'OrderBy' : '1', 'PageIndex' : '1'})
    html = opener.open(URL, data=data)
    soup = BeautifulSoup(html.read())
    spanPage = soup.findAll('span', {'class':'page'})
    spanEndPage = spanPage[len(spanPage)-1]
    href = spanEndPage.findAll('a')[0]['href']
    maxPage = href[20:]
    maxPage = int(maxPage[:len(maxPage)-1])
    del opener, data, html, soup, spanPage, spanEndPage, href
    return maxPage

def crawlAllEbook():
    """
    crawl url and totalchap of all ebook
    :return: list Object Ebook
    """
    print "Run crawlAllEbook()"
    try:
        listEbook = []
        for i in range(maxPage()):
            if i!=0:
                opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
                data = urllib.urlencode({'Url' : 'tatca', 'OrderBy' : '1', 'PageIndex' : i})
                html = opener.open(URL, data=data)
                soup = BeautifulSoup(html.read())
                divlist = soup.findAll('div', {'class':'list'})
                pNulls = divlist[0].findAll('p',{'class':''})

                for pNull in pNulls:
                    spans = pNull.findAll('span')
                    url = "http://blogtruyen.com"+spans[0].findAll('a')[0]['href']
                    totalChap = int(spans[1].text)
                    ebook = Ebook()
                    ebook.url = url
                    ebook.totalchap = totalChap
                    listEbook.append(ebook)
                print "====> next  %d" % i
            else:
                pass
        print "End crawlAllEbook()"
        return listEbook
    except:
        print "error! disconnect with server (method: crawlAllEbook )"


def crawlInforEbook():
    #id = ebook.id
    #url = ebook.url
    url = 'http://blogtruyen.com/truyen/kuroko-no-basket-doujinshi'
    print "----->  crawlInforEbook()"
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html.read())

    h1 = soup.findAll('h1', {'class':'entry-title'})
    name = h1[0].text

    divcontent = soup.findAll('div',{'class':'content'})
    description = divcontent[0].text

    divthumbnail = soup.findAll('div', {'class':'thumbnail'})
    cover =  divthumbnail[0].findAll('img')[0]['src']

    divDecription = soup.findAll('div',{'class':'description'})
    pNulls = divDecription[0].findAll('p')
    for pNull in pNulls:
        if pNull.text.startswith('Ngu'):
            print pNull

crawlInforEbook()