# -*- coding: cp936 -*-
import urllib2, BeautifulSoup

def lookup(word):
    res = urllib2.urlopen('http://www.iciba.com/' + word).read()
    if res.find("词库中没有") >= 0:
        print "Not found"
        return
    soup = BeautifulSoup.BeautifulSoup(res)
    meaning = soup.findAll('label')
    if not meaning:
        print "Not found"
        return
    del meaning[0]
    for m in meaning:
        print m.text

def lookup2(word):
    res = urllib2.urlopen('http://dictionary.reference.com/browse/' + word).read()
    soup = BeautifulSoup.BeautifulSoup(res)
    meaning = soup.findAll('div',{'class':'dndata'})
    for m in meaning:
        print m.text      

if __name__ == '__main__':
    lookup2('eclipse')
