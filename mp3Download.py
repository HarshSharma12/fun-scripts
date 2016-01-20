# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:05:59 2016
@author: HarshSharma12

A general bs4 and requests example
(Uses proxy)
"""
from bs4 import BeautifulSoup
import requests
import urllib2

https_proxy = "HTTP PROXY"
http_proxy  = "HTTPS PROXY"
ftp_proxy   = "FTP PROXY"
proxyDict = { 
               "http"  : http_proxy, 
               "https" : https_proxy, 
               "ftp"   : ftp_proxy
             }

fid = open('listOfSongs.txt','r')
listOfSongs = fid.readlines()
fid.close()
skipped=[]
for song in listOfSongs:
    filename = song.replace('\n','')
    if (filename==''):
        exit()
    url = 'https://mp3skull.yoga/search_db.php?q='+filename.replace(' ','+')+'&fckh=1ee2bc77261355b033536ff86647cad0'

    r = requests.get(url, proxies=proxyDict)
    soup = BeautifulSoup(r.text)
    songs = str(soup.findAll('div', class_='left'))
    songs = songs.split(',')
    
    toBe=[]
    bitrates = []
    
    for x in songs:
        try:
            startLoc = x.find('<br/>')
            bitrate = int(x[startLoc-8:startLoc-5])
            if(bitrate>200):
                if(int(x[startLoc+5])>1):
                    toBe.append(songs.index(x)+1)
                    bitrates.append(bitrate)
        except(ValueError):
            print 'Oops, ValueError'
            
    
    print filename    
    print toBe
    print bitrates
    try:
        downloadClass = 'show'+str(toBe[bitrates.index(max(bitrates))])
        
        newSoup = soup.find('div', class_=downloadClass)
        downButton=newSoup.find('div', class_='download_button')
        final = downButton.find('a', href=True)
        downURL = str(final['href'])
        title = str(newSoup.find('div', class_='mp3_title').text)
        
        proxy = urllib2.ProxyHandler(proxyDict)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        
        with open(title+' + '+filename+'.mp3','wb') as f:
            f.write(urllib2.urlopen(downURL).read())
            f.close()
        finished.append(filename)
    except:
        skipped.append(filename)
        print 'Skipping song '+filename

fid=open('skipped.txt', 'w')
for x in skipped:
    fid.write(x)
    fid.write('\n')
fid.close()

fid=open('finished.txt', 'w')
for x in finished:
    fid.write(x)
    fid.write('\n')
fid.close()
