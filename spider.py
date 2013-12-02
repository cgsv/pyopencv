from sgmllib import SGMLParser
import pprint
import urllib

class URLLister(SGMLParser):
    def reset(self):                              
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):                     
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)

def getURL(url):
    try:
        usock = urllib.urlopen(url)
    except:
        print 'get url exception'
        return []
    parser = URLLister()
    parser.feed(usock.read())    
    usock.close()
    parser.close()
    urls = parser.urls
    return urls

def spider(startURL, depth):
    i = 0
    global num      
    if depth <= i:    
       return 0
    else:
       urls = getURL(startURL)    
       if len(urls) > 0:
            for url in urls:        
                print url, num
                num = num + 1
                spider(url,depth - 1)
       else:
                return 0
    return 1

num = 0
#spider("http://www.sina.com.cn/",2)
spider("http://www.baidu.com", 2)

