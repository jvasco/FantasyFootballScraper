import requests
import csv
import smtplib

from email.mime.text import MIMEText

from BeautifulSoup import BeautifulSoup

url = 'http://www.espn.com/fantasy/football/story/_/page/18rankspreseason300ppr/2018-fantasy-football-ppr-rankings-top-300'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
##divs = soup.findAll("div", {"class": "article-body"})
table = soup.findAll("table", {"class": "inline-table"})

listofrows = []
for row in table[1].findAll('tr'):
    listofcells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        listofcells.append(text)
    listofrows.append(listofcells)
    ##print row.prettify()
    
outfile = open("./results.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Player", "Position", "Team", "Position Ranking"])
writer.writerows(listofrows)

##print table