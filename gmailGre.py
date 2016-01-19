#!/usr/local/bin/python2.7
"""
Created on Fri Dec 18 17:00:23 2015
@author: HarshSharma12

Sends a daily email containing thirty 
words from the Barron's GRE word list.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.Utils import COMMASPACE
from email.MIMEText import MIMEText
import time


numOfWords = 15
totalWords = 4843
fid = open('barron1.txt','r')
wordList = []
for i in range(numOfWords):
    wordList.append(fid.readline())

remaining = fid.readlines()
print wordList
fid.close()

fid = open('barron1.txt', 'w')
for a in remaining:
    fid.write(a)
fid.close()

words = []
definitions = []

for w in wordList:
    words.append(w[:w.index('\t')].upper())
    definitions.append(w[w.index('\t')+1:])

#print definitions
def2 = []
#print '-----------------------------'
for s in definitions:
    ch  = '\n'
    if ch in s :
        s = s.replace(ch,'')
    ch  = '\t'
    if ch in s :
        s = s.replace(ch,'')
    def2.append(s)

#print def2


server = smtplib.SMTP()
server.connect('smtp.gmail.com',587) # for eg. host = 'smtp.gmail.com', port = 587
server.ehlo()
server.starttls()
server.login('FromAddr', 'password')

fromaddr = 'FromAddr@...'
tolist = ['ToAddr1@...', 'ToAddr2@...']
sub = 'GRE Words for '+time.ctime()[:10]
html1 = """
<html>
  <head><style>
  p{
  font-size:24px;
  }
table, th, td {
    border: 1px solid black;
    font-size:18px;
}

</style></head>
  <body>
    <p>These words have been taken from the Barron's word list(Total 4843 words). Everyday (Starting 20/12/2015) 
    %s words will be sent at 5 AM IST (till the list is exhausted)<br>
    The words for today are:
    <table>
"""%str(numOfWords)

for i in range(len(words)):
    text1 = '<tr><td bgcolor="#CDECFF"><b>'+words[i]+'</b></td><td bgcolor="#EDEDEC">'+def2[i]+'</td></tr>'
    print text1
    html1 = html1+text1

html2 = """</table> </p>
  </body>
</html>
"""

html = html1+html2

msg = MIMEMultipart('alternative')
msg['From'] = fromaddr
msg['To'] = COMMASPACE.join(tolist)
msg['Subject'] = sub
part1 = MIMEText(html, 'html')
msg.attach(part1)


server.sendmail(fromaddr,tolist,msg.as_string())
server.quit()
