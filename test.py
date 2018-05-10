import requests;
import csv;
from bs4 import BeautifulSoup
from time import sleep

listA = [];

def requesturl(n):
      #reqcode = 0;
      findID = 0;

      ####### requests #######

      # "https://www.amazon.com/s/ref=?url=search-alias%3Daps&field-keywords=cat+litter" #  - url requert 작동 안함 (보안)
      # response = requests.get('https://www.amazon.com/Fresh-Step-Multi-Cat-Freshness-Clumping/product-reviews/B0784SX6XX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
      url = "https://www.amazon.com/Fresh-Step-Multi-Cat-Freshness-Clumping/product-reviews/B0784SX6XX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="
      url = url + str(n);
      response = requests.get(url);
      while int(response.status_code) == 503:
            sleep(3);
            response = requests.get(url);
      # page 처리는  + &pageNumber= 페이지 숫자
      html = response.text

      # print(html) # check it
      print(response) # check it
      print(url)
      #reqcode = response.status_code;

      ####### parser #######

      soup = BeautifulSoup(html, 'html.parser')
      # for tag in soup.select('div[class=review-views]'):
      # a = soup.findAll("div",class_="a-section celwidget") ## 전체버전
      # a = soup.find("div",class_="a-section celwidget") ## 한개의 리뷰
      # a = soup.find("span",class_="a-icon-alt") ##  리뷰
      # b = soup.find("span",class_="a-size-base review-text") ## 별점

      # print(a)
      # print(b)
      if soup.find("div", class_="a-section celwidget") :
            findID = 1;
      else :
            findID = 0;

      # print(tag)
      for tag1 in soup.findAll("div", class_="a-section celwidget"):
            soup1 = BeautifulSoup(str(tag1), 'html.parser')
            soup2 = BeautifulSoup(str(tag1), 'html.parser')
            a = soup1.find("span", class_="a-icon-alt")
            b = soup2.find("span", class_="a-size-base review-text")
            tempA = str(a.text);
            tempB = str(b.text);
            tempA = tempA.replace(',','_');
            tempB = tempB.replace(',','_');
            tempStr = tempA + "," + tempB;
            listA.append(tempStr);
            #print(a.text)
            #print(b.text)
            #print('-----------------------------------------------------');

      ##### test #####

      # a-section a-spacing-none review-views celwidget
      # cm-cr-dp-review-list
      # for tag in soup.select('div[class=a-section a-spacing-none review-views celwidget]'):
      #      a = tag.text.strip()
      #      print(a)

      # a = soup.select('div#cm-cr-dp-review-list')
      ###
      # a = soup.findAll('body')
      # b = soup.findAll('div', attrs = { "class" : "a-section a-spacing-none review-views celwidget"})
      # print(a)

      return findID;


def filesave(a):
      f = open('output.csv', 'w', encoding='utf-8', newline='')
      wr = csv.writer(f)
      for j in a:
            wr.writerow([j])
      f.close()

i = 1;
listA.clear();

while True :
 test321 = requesturl(i);
 print(str(i) + '|' + str(test321));
 if int(test321) == 0 :
      break;
 print('###########################################');
 i = i+1;

filesave(listA);




