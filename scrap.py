# -*- coding: utf-8 -*-
"""
//*[@id="lastPrice"]
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL ='https://economictimes.indiatimes.com/bharat-petroleum-corporation-ltd/stocks/companyid-11941.cms'
head = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
def check():
    page = requests.get(URL ,headers=head)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    #title= soup.find(id='').get_text()
    price1 = soup.find(id='nseTradeprice').get_text()
    price2 = soup.find(id='nseTradeprice').get_text()
    price3 = soup.find(id='nseTradeprice').get_text()
    price4 = soup.find(id='nseTradeprice').get_text()

    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('user@gmail.com','egihvbhplaplsqkf')
    sub = 'price of shares'
    body= "check: link"
    msg = f"subject:{sub} \n \n {body}"

    server.sendmail(
            'user@gmail.com',
            'user0@gmail.com',
             msg

            )
    print('sent mail')
    server.quit()
    i=5
    while i>3:
        check()
        i -= 1
    #time.sleep(3600)
